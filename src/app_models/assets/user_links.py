from typing import Optional
from sqlmodel import SQLModel, Field




class UserGroupLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    group_id: Optional[int] = Field(
        default=None, foreign_key="group.id", primary_key=True
    )


class UserClientRoleLink(SQLModel, table=True):
    user_id: Optional[int] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    client_role_id: Optional[int] = Field(
        default=None, foreign_key="client_role.id", primary_key=True
    )
