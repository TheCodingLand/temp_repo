from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Column, SQLModel, String


from typing import Optional
from sqlmodel import Relationship, SQLModel, Field
from .email_links import EmailCategoryLink 
if TYPE_CHECKING:
    from .email import Email
class CategoryBase(SQLModel):
    name: str = Field(..., max_length=50, description="Category Name", sa_column=Column("email", String, unique=True))
  
class Category(CategoryBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    emails: List["Email"] = Relationship(back_populates="categories", link_model=EmailCategoryLink)


class CategoryCreate(CategoryBase):
    pass

class CategoryGet(SQLModel):
    id: Optional[int] = Field(default=None)

class CategoryUpdate(CategoryBase):
    id: Optional[int] = Field(default=None, primary_key=True)
