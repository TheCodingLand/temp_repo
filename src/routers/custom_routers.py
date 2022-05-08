
from typing import TYPE_CHECKING, cast

from sqlmodel import Session


from db import get_db


if TYPE_CHECKING:
    from fastapi import FastAPI
    
from fastapi import Depends
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from appmodels.email.email import Email, EmailBase
from appmodels.email.contact import Contact
from appmodels.email.email_links import SentBCCContactLink,SentToContactLink, SentCCContactLink, EmailAttachmentLink, EmailCategoryLink
from appmodels.email.email import EmailCreate, EmailGet, EmailUpdate

import logging

email_router = SQLAlchemyCRUDRouter(
        schema=EmailUpdate,
        create_schema=EmailCreate,
        update_schema=EmailUpdate,
        db_model=Email,
        db=get_db,
        prefix='email'
    )  


@email_router.post("")
def custom_create_email_router(email: EmailCreate,  session: Session = Depends(get_db)):

    email_base = EmailBase(**email.dict(exclude_unset=True, exclude_none=True))
    db_email = Email(**email_base.dict(exclude_unset=True, exclude_none=True))
    many_to_many_contact_fields=['to_recipients', 'cc_recipients', 'bcc_recipients']
    for attr in many_to_many_contact_fields:
        contacts= []
        for contact in cast(List[Contact],getattr(email, attr)):
            if contact.email_address is not None:
                c = session.query(Contact).filter_by(email_address=contact.email_address).one()
                if contact is not None:
                    logging.warning(f"Could not find contact with email_address : '{contact.email_address}'")
                    contacts.append(c)
        print (contacts)
        setattr(db_email, attr,  contacts)
    print(db_email)
    session.add(db_email)
    session.commit()
    session.refresh(db_email)            



def include_custom_routers(app: "FastApi"):
    
    app.include_router(email_router)
