from typing import TYPE_CHECKING, List, Optional
from click import Group
from sqlmodel import Column, Relationship, SQLModel, Field, String

from appmodels.access_control.group import Group

if TYPE_CHECKING:
    from appmodels.airflow.dag_run import DagRun


class DagBase(SQLModel):
    dag_id: str = Field(..., max_length=150, sa_column=Column("dag_id", String, unique=True))
    description: Optional[str] = Field("", max_length=300)
    owner_id: Optional[int] = Field(None, foreign_key='group.id', sa_column_kwargs={"nullable":True})
    
    
class Dag(DagBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    runs: List["DagRun"] = Relationship(back_populates="dag")
    owner: List["Group"] = Relationship()

class GetDagWithTasks(SQLModel):
    id: int
  
class DagCreate(DagBase):
    pass
    

class GetDagWithRuns(DagBase):
    id: int
    runs: List["DagRun"]
   
class DagUpdate(DagCreate):
    id: int

from .dag_run import DagRun
GetDagWithRuns.update_forward_refs()


