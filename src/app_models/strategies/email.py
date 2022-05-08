
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

from sqlmodel import Relationship, SQLModel, Field, String, Column, Text
from .contact import Contact, ContactUpdate
from .attachment import Attachment
from .category import Category
from .email_links import SentToContactLink, SentCCContactLink, SentBCCContactLink, EmailAttachmentLink,EmailCategoryLink

if TYPE_CHECKING:
    #from appmodels.management.service_family import ServiceFamily
    #from appmodels.airflow.dag import Dag
    pass


class EmailBase(SQLModel):
    mailbox_id: int = Field(..., foreign_key="mailbox.id")
    message_id: str = Field(..., max_length=200, description="Message ID from exchange", sa_column=Column("email", String, unique=True))
    change_id: str = Field(..., max_length=200, description="Change ID from exchange")
    datetime_received: datetime = Field(..., description="Datetime or arrival of the message")
    conversation_id: str = Field(..., max_length=200, description="Conversation ID from exchange")
    subject: str = Field(..., max_length=200, description="Subject of the message")
    body_text: str = Field("", description="Text body of the email", sa_column=Column("body_text", Text))
    body_html: str = Field("", description="HTML body of the email", sa_column=Column("html_text", Text))
    sender_id: int = Field(..., foreign_key="contact.id")
    
    related_dag_task_id: int = Field(..., foreign_key="dag_task_run.id")


class Email(EmailBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    to_recipients: List["Contact"] = Relationship(back_populates="in_to_recipients_of", link_model=SentToContactLink)
    cc_recipients: List["Contact"] = Relationship(back_populates="in_cc_recipients_of", link_model=SentCCContactLink)
    bcc_recipients: List["Contact"] = Relationship(back_populates="in_bcc_recipients_of", link_model=SentBCCContactLink)
    attachments: List["Attachment"] = Relationship(back_populates="in_attachment_of_emails", link_model=EmailAttachmentLink)
    categories: List["Category"] = Relationship(back_populates="emails", link_model=EmailCategoryLink)
    
class EmailCreate(EmailBase):
    to_recipients: List["ContactUpdate"]
    cc_recipients: List["ContactUpdate"]
    bcc_recipients: List["ContactUpdate"] 
    #attachments: List["AttachmentUpdate"]  
    #categories: List["CategoryUpdate"]   



class EmailGet(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    

class EmailUpdate(EmailCreate):
    id: Optional[int] = Field(default=None, primary_key=True)
