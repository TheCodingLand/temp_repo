
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Column, SQLModel, String


from typing import Optional
from sqlmodel import Relationship, SQLModel, Field

from appmodels.email.mail_server import MailServer
    

class MailboxBase(SQLModel):
    address: str = Field(..., max_length=100, description="Email address", sa_column=Column("address", String, unique=True))
    mail_server_id: int = Field(..., foreign_key="mail_server.id")

class Mailbox(MailboxBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    mail_server: MailServer = Relationship(back_populates="mailboxes")

class MailboxCreate(MailboxBase):
    pass

class MailboxGet(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)

class MailboxUpdate(MailboxBase):
    id: Optional[int] = Field(default=None, primary_key=True)
