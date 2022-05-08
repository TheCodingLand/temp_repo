from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Column, SQLModel, String


from typing import Optional
from sqlmodel import Relationship, SQLModel, Field
from .services_links import ServiceSolutionLink
if TYPE_CHECKING:
    from .service import Service

class SolutionBase(SQLModel):
    name: str = Field(..., sa_column=Column("service_name", String, unique=True))
    instances: int = Field()
    
    
class Solution(SolutionBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    services: List["Service"] = Relationship(back_populates="solutions", link_model=ServiceSolutionLink)


class SolutionCreate(SolutionBase):
    pass

class SolutionGet(SQLModel):

    id: Optional[int] = Field(default=None)

class SolutionUpdate(SolutionBase):
    id: Optional[int] = Field(default=None, primary_key=True)



