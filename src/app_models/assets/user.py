

from typing import List, Optional

from sqlmodel import Column, Field, SQLModel, Relationship, String

from .user_links import UserClientRoleLink, UserGroupLink
from .group import  Group
from .client_roles import ClientRole

class UserBase(SQLModel):
    username: str = Field(..., max_length=150, sa_column=Column("username", String, unique=True))
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email_address: Optional[str] = Field(...)
    

class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    groups: List[Group] = Relationship(back_populates="users", link_model=UserGroupLink)
    client_roles: List[ClientRole] = Relationship(back_populates="users", link_model=UserClientRoleLink)


class UserWithGroups(UserBase):
    groups: List[Group]
    client_roles: List[ClientRole] 
  
UserWithGroups.update_forward_refs()


"""
  def is_member_of(self, group_name: str):
        for group in self.groups:
            if group.name==group_name:
                return True
        return False

    def has_role(self, role_name: str):
        for role in self.client_roles:
            if role.name==role_name:
                return True
        return False"""