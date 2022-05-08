from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Column, SQLModel, String


from typing import Optional
from sqlmodel import Relationship, SQLModel, Field

if TYPE_CHECKING:
    from .service import Service

class ServiceOwnerBase(SQLModel):
    name: str = Field(..., sa_column=Column("service_name", String, unique=True))
    company_name: str = Field(..., max_length=150, description="billing code for this service")
    
    
class ServiceOwner(ServiceOwnerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    services: List["Service"] = Relationship(back_populates="owner")


class ServiceOwnerCreate(ServiceOwnerBase):
    pass

class ServiceOwnerGet(SQLModel):
    id: Optional[int] = Field(default=None)

class ServiceOwnerWithServices(SQLModel):
    id: Optional[int] = Field(default=None)
    services: List["Service"]

class ServiceOwnerUpdate(ServiceOwnerBase):
    id: Optional[int] = Field(default=None, primary_key=True)



