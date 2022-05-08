from typing import TYPE_CHECKING, ForwardRef, List, Optional, Any

from sqlmodel import Column, Relationship, SQLModel, Field, String

from .user_links import UserGroupLink


class GroupBase(SQLModel):
    name: str = Field(..., max_length=150, sa_column=Column("name", String, unique=True))

class Group(GroupBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    users: List["User"] = Relationship(back_populates="groups", link_model=UserGroupLink)
    
class GroupWithUsers(GroupBase):
    users: List["UserBase"] = []
    

"""class GroupOwner(SQLModel, table=True):
    #Defines the relashionship from any table to a group
    __tablename__ = "group_owner_model"

    id: Optional[int] = Field(default=None, primary_key=True)

    group_id: int = Field(
        default=None, foreign_key="group.id", primary_key=True
    )
    object_type: str = Field(..., max_length=150)
    object_id: int = Field(...)
    object: Any = generic_relationship(object_type, object_id)
"""


