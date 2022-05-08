
from typing import List, Optional
from sqlmodel import Column, Relationship, SQLModel, Field, String

from appmodels.management.service import Service


#BASE
class ServiceFamilyBase(SQLModel):
    family_name =  str = Field(..., max_length=150, description="Service Familily or main group", sa_column=Column("family_name", String, unique=True))


class ServiceFamily(ServiceFamilyBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    services: List[Service] = Relationship(back_populates='family')


class ServiceFamilyCreate(ServiceFamilyBase):
    pass


class ServiceFamilyGet(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    

class ServiceFamilyUpdate(ServiceFamilyBase):
    id: Optional[int] = Field(default=None, primary_key=True)

  
