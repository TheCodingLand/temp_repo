from typing import TYPE_CHECKING, ForwardRef, List, Optional, Any

from sqlmodel import Column, Relationship, SQLModel, Field, String

from .user_links import UserClientRoleLink
if TYPE_CHECKING:
    from appmodels.access_control.user import UserBase, User
class ClientRoleBase(SQLModel):
    name: str = Field(..., max_length=150, sa_column=Column("name", String, unique=True))

class ClientRole(ClientRoleBase, table=True):
    __tablename__ = "client_role"
    id: Optional[int] = Field(default=None, primary_key=True)
    users: List["User"] = Relationship(back_populates="client_roles", link_model=UserClientRoleLink)
    
class ClientRoleWithUsers(ClientRoleBase):
    users: List["UserBase"]
