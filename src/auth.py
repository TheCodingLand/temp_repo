

from typing import Any, Dict, List, Optional, Tuple, cast
from fastapi.security import OAuth2AuthorizationCodeBearer, SecurityScopes
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from jose.constants import ALGORITHMS
from pydantic import BaseModel
import requests
import sys
from sqlalchemy.orm.exc import NoResultFound
from sqlmodel import Session
from appmodels.access_control.user import UserWithGroups, User
from db import get_db
from appmodels.access_control.group import Group
import logging

from appmodels.access_control.client_roles import ClientRole
from utils import get_or_create

class TokenData(BaseModel):
    preferred_username: str
    member_of: List[str] =  []
    client_roles: List[str] =  []
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    email: Optional[str] = None


oauth2_scheme = OAuth2AuthorizationCodeBearer(
    tokenUrl="https://auth.next-in-tech.fr/auth/realms/AirFlowFrontend/protocol/openid-connect/token",
    authorizationUrl="https://auth.next-in-tech.fr/auth/realms/AirFlowFrontend/protocol/openid-connect/auth",
    scopes={"admin": "Can add dags", "manager": "Read items, run dags.", "access": "Read dag runs"}
    )

# Why doing this?
# Because we want to fetch public key on start
# Later we would verify incoming JWT tokens
try:
    r = requests.get("https://auth.next-in-tech.fr/auth/realms/AirFlowFrontend",
                     timeout=3)
    r.raise_for_status()
    response_json = r.json()
except requests.exceptions.HTTPError as errh:
    print("Http Error:", errh)
    sys.exit(1)
except requests.exceptions.ConnectionError as errc:
    print("Error Connecting:", errc)
    sys.exit(1)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
    sys.exit(1)
except requests.exceptions.RequestException as err:
    print("OOps: Something Else", err)
    sys.exit(1)

#oauth2_scheme_form = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = f'-----BEGIN PUBLIC KEY-----\r\n{response_json["public_key"]}\r\n-----END PUBLIC KEY-----'


async def get_current_user(security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)) -> TokenData:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = cast(Dict[str,Any], jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHMS.RS256],
                             options={"verify_signature": True, "verify_aud": False, "exp": True}))
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(**payload)
    except JWTError as e:
        print(e)
        raise credentials_exception
    return token_data

async def get_current_active_user(token_data: TokenData = Depends(get_current_user), session: Session = Depends(get_db)) -> User:
    logging.error(token_data)
    # fill in groups
    knwon_groups = session.query(Group).all()
    grp_membership: List[Group] = []
    for group_name in token_data.member_of:
        matches: List[Group] = list(filter(lambda x: x.name == group_name, knwon_groups))
        if len(matches) == 0:
            group = Group(name=group_name)
            session.add(group)
            session.commit()
        else:
            group = matches[0]
        grp_membership.append(group)
    
    # fill in client_roles
    logging.warning(grp_membership)
    knwon_client_roles = session.query(ClientRole).all()
    cr_membership: List[ClientRole] = []
    for client_role_name in token_data.client_roles:
        matches: List[ClientRole] = list(filter(lambda x: x.name == client_role_name, knwon_client_roles))
        if len(matches) == 0:
            client_role = ClientRole(name=client_role_name)
            session.add(client_role)
            session.commit()
        else:
            client_role = matches[0]
        cr_membership.append(client_role)
    logging.warning(cr_membership)
    if token_data.email is None:
        logging.error("Cannot create a user without a valid email address.")
        raise ValueError
    
   
    token_user_data = {"username":token_data.preferred_username, "first_name":token_data.given_name, "last_name":token_data.family_name, "email_address": token_data.email }
   
    
    #airflow-react-frontend-dev
    logging.error(token_user_data)
    current_user = find_or_create_user_and_update(session, token_data.preferred_username, token_user_data=token_user_data,groups=grp_membership, roles=cr_membership )
    
    
    #session.add(current_user)
    #session.commit()

    return current_user


def find_or_create_user_and_update(session: Session, username: str, token_user_data: Dict[str, Any], groups: List[Group], roles: List[ClientRole] ) -> User:
    """Creates a user and returns it, or if it already exists, returns the exising user. True if user was created, False if not"""
    try:
        user: User = session.query(User).filter_by(username=username).one()
        session.query(User).filter_by(username=username).update(token_user_data)
    except NoResultFound:
        user = User(**token_user_data)
        session.add(user)
    if user.groups != groups:
        user.groups = groups
    if user.client_roles != roles:
        user.client_roles = roles 
    session.commit()
    return user

    