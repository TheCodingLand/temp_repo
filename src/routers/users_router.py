from fastapi import APIRouter, Depends
from auth import  get_current_active_user
from appmodels.access_control.user import User



users_router = APIRouter()

@users_router.get("/users/me/", response_model=User)
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@users_router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

"""
@users_router.get("/user/roles", tags=["secured-endpoint"])
def user_roles(user: User = Depends(auth.get_current_user)):
    return f'{user.roles}'


@users_router.get("/manager", tags=["secured-endpoint"])
def premium(user: User = Depends(auth.get_current_user(required_roles=["manager"]))):
    return f'Hi manager user {user}'

"""