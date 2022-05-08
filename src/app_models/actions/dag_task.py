
from typing import List, Optional
from sqlmodel import Column, Relationship, SQLModel, Field, String


# BASE
class DagTaskBase(SQLModel):
    task_id: str = Field(..., max_length=150,  sa_column=Column("task_id", String, unique=True))
    name: str = Field(..., max_length=150)
    description: str = Field(..., max_length=300)
    dag_id: int = Field(..., foreign_key='dag.id')


# DB
class DagTask(DagTaskBase, table=True):
    __tablename__ = "dag_task"
    id: Optional[int] = Field(default=None, primary_key=True)
    runs: List["DagTaskRun"] = Relationship(back_populates="dag_task")

# VIEWS
class DagTaskGet(SQLModel):
    id: int

   
class DagTaskCreate(DagTaskBase):
    pass

   
class DagTaskUpdate(DagTaskBase):
    id: int


