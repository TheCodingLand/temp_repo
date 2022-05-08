    
from datetime import datetime
from typing import Optional
from sqlmodel import Column, Relationship, SQLModel, Field, String


# BASE
class DagTaskRunBase(SQLModel):
    
    airflow_task_run_id: str = Field(..., max_length=150,  sa_column=Column("airflow_task_run_id", String, unique=True))
    name: str = Field(..., max_length=150)
    start_date: datetime = Field(...)
    end_date: Optional[datetime] = Field(...)
    state: str = Field(..., max_length=100)
    dag_task_id: int = Field(..., foreign_key='dag_task.id')
    dag_run_id: int = Field(..., foreign_key='dag_run.id')
    


# DB
class DagTaskRun(DagTaskRunBase, table=True):
    __tablename__ = "dag_task_run"
    id: Optional[int] = Field(default=None, primary_key=True)
    dag_task: "DagTask" = Relationship(back_populates="runs")

# VIEWS
class DagTaskRunGet(SQLModel):
    id: int


class DagTaskRunCreate(DagTaskRunBase):
    pass

class DagTaskRunUpdate(SQLModel):
    id: int
    end_date: datetime = Field(...)
    state: str = Field(..., max_length=100)
