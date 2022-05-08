from typing import Optional
from pydantic import EmailStr
from sqlmodel import Field, SQLModel

class MailServer(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str

class Mailbox(SQLModel, table=True):        
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: EmailStr
    mail_server: Optional[MailServer]
