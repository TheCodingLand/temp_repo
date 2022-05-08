
from typing import TYPE_CHECKING, List, Optional
from pydantic import BaseModel

from sqlmodel import Column, SQLModel, String

from .email_links import SentCCContactLink, SentToContactLink, SentBCCContactLink
from typing import Optional
from sqlmodel import Relationship, SQLModel, Field
if TYPE_CHECKING:
    from .email import Email

class ContactBase(SQLModel):
    first_name: str = Field(..., max_length=100, description="First Name")
    last_name: str = Field(..., max_length=100, description="Last Name")
    email_address: str = Field(..., max_length=100, description="Email address", sa_column=Column("email_address", String, unique=True))
    
class Contact(ContactBase, table=True):
    __tablename__ = 'contact'
    id: Optional[int] = Field(default=None, primary_key=True)
    in_to_recipients_of: List["Email"] = Relationship(back_populates="to_recipients", link_model=SentToContactLink)
    in_cc_recipients_of: List["Email"] = Relationship(back_populates="cc_recipients", link_model=SentCCContactLink)
    in_bcc_recipients_of: List["Email"] = Relationship(back_populates="bcc_recipients", link_model=SentBCCContactLink)

class ContactCreate(ContactBase):    
    pass

class ContactGet(SQLModel):
    id: Optional[int] = Field(default=None)

class ContactUpdate(BaseModel):
    """Email address is the real unique identifyer of a contact from the API standpoint"""
    id: Optional[int] = Field(None)
    first_name: Optional[str] = Field(None, max_length=100, description="First Name")
    last_name: Optional[str] = Field(None, max_length=100, description="Last Name")
    email_address: str = Field(None, max_length=100,  description="Email address")
