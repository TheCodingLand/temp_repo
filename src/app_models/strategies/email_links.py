
from typing import Optional
from sqlmodel import Field, SQLModel


class SentToContactLink(SQLModel, table=True):
    email_id: Optional[int] = Field(
        default=None, foreign_key="email.id", primary_key=True
    )
    contact_id: Optional[int] = Field(
        default=None, foreign_key="contact.id", primary_key=True
    )

class SentCCContactLink(SQLModel, table=True):
    email_id: Optional[int] = Field(
        default=None, foreign_key="email.id", primary_key=True
    )
    contact_id: Optional[int] = Field(
        default=None, foreign_key="contact.id", primary_key=True
    )   

class SentBCCContactLink(SQLModel, table=True):
    email_id: Optional[int] = Field(
        default=None, foreign_key="email.id", primary_key=True
    )
    contact_id: Optional[int] = Field(
        default=None, foreign_key="contact.id", primary_key=True
    )

class EmailCategoryLink(SQLModel, table=True):
    email_id: Optional[int] = Field(
        default=None, foreign_key="email.id", primary_key=True
    )
    category_id: Optional[int] = Field(
        default=None, foreign_key="category.id", primary_key=True
    )

class EmailAttachmentLink(SQLModel, table=True):
    email_id: Optional[int] = Field(
        default=None, foreign_key="email.id", primary_key=True
    )
    attachment_id: Optional[int] = Field(
        default=None, foreign_key="attachment.id", primary_key=True
    )
