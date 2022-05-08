
from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Column, SQLModel, LargeBinary


from typing import Optional
from sqlmodel import Relationship, SQLModel, Field
from .email_links import EmailAttachmentLink    
if TYPE_CHECKING:
    from .email import Email

class AttachmentBase(SQLModel):
    content: bytes = Field(..., sa_column=Column("content", LargeBinary))
    inline: bool = Field(False)
    mimetype: str = Field(..., max_length=100, description="Mime Type")
    file_path: str = Field(..., max_length=200, description="Last Name")
    file_name: str = Field(..., max_length=200, description="File Name")
    
class Attachment(AttachmentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    in_attachment_of_emails: List["Email"] = Relationship(back_populates="attachments", link_model=EmailAttachmentLink)


class AttachmentCreate(AttachmentBase):
    pass

class AttachmentGet(SQLModel):
    id: Optional[int] = Field(default=None)

class AttachmentUpdate(AttachmentBase):
    id: Optional[int] = Field(default=None, primary_key=True)