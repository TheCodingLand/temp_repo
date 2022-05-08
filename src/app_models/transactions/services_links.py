

from typing import Optional

from sqlmodel import Field, SQLModel


class ServiceSolutionLink(SQLModel, table=True):
    service_id: Optional[int] = Field(
        default=None, foreign_key="service.id", primary_key=True
    )
    solution_id: Optional[int] = Field(
        default=None, foreign_key="solution.id", primary_key=True
    )   
