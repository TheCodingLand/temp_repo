
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Column, SQLModel, String


from typing import Optional
from sqlmodel import Relationship, SQLModel, Field


if TYPE_CHECKING:
    from appmodels.management.service_family import ServiceFamily
    from appmodels.airflow.dag import Dag
    

class ServiceBase(SQLModel):
    dag_id: int = Field(..., foreign_key="dag.id")
    service_family_id: int = Field(..., foreign_key="service_family.id")
    billing_code: str = Field(..., max_length=50, description="billing code for this service")
    service_name: str = Field(..., max_length=150, description="Name of an automated process", sa_column=Column("service_name", String, unique=True))
    


class Service(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    dag: "Dag" = Relationship(back_populates="dag")
    service_family: "ServiceFamily" = Relationship(back_populates="services")


class ServiceCreate(ServiceBase):
    pass


class ServiceGet(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    

class ServiceUpdate(ServiceBase):
    id: Optional[int] = Field(default=None, primary_key=True)

