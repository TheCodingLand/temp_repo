from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Column, SQLModel, String


from typing import Optional
from sqlmodel import Relationship, SQLModel, Field
if TYPE_CHECKING:
    from appmodels.email.mailbox import Mailbox
    

class MailServerBase(SQLModel):
    url: str = Field(..., max_length=100, description="Url of the server", sa_column=Column("url", String, unique=True))
    
class MailServer(MailServerBase, table=True):
    __tablename__ = 'mail_server'
    id: Optional[int] = Field(default=None, primary_key=True)
    mailboxes : List["Mailbox"] = Relationship(back_populates="mail_server")

class MailServerCreate(MailServerBase):
    pass

class MailServerGet(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)

class MailServerUpdate(MailServerBase):
    id: Optional[int] = Field(default=None, primary_key=True)
