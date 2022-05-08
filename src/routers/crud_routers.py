from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from fastapi import FastAPI
from fastapi import Depends
from db import get_db
from auth import get_current_user, get_current_active_user
from fastapi_crudrouter import SQLAlchemyCRUDRouter
from appmodels.email.contact import Contact, ContactCreate, ContactUpdate
from appmodels.email.mail_server import MailServer, MailServerCreate, MailServerUpdate
from appmodels.email.mailbox import Mailbox, MailboxCreate, MailboxUpdate
from appmodels.email.attachment import Attachment, AttachmentCreate, AttachmentUpdate
from appmodels.email.category import Category, CategoryUpdate,CategoryCreate

from appmodels.airflow.dag import Dag, DagCreate, DagUpdate, GetDagWithRuns
from appmodels.airflow.dag_run import DagRun, DagRunCreate, DagRunUpdate
from appmodels.airflow.dag_task import DagTask, DagTaskCreate, DagTaskUpdate
from appmodels.airflow.dag_task_run import DagTaskRun, DagTaskRunCreate, DagTaskRunUpdate
from appmodels.access_control.user import User, UserBase
from appmodels.access_control.group import Group, GroupBase, GroupWithUsers
from appmodels.access_control.client_roles import ClientRole, ClientRoleBase, ClientRoleWithUsers


GroupWithUsers.update_forward_refs(UserBase=UserBase)
ClientRoleWithUsers.update_forward_refs(UserBase=UserBase)

def include_crud_routers(app: "FastAPI"):
    app.include_router(SQLAlchemyCRUDRouter(
        schema=ClientRoleWithUsers,
        create_schema=ClientRoleBase,
        update_schema=ClientRoleBase,
        db_model=ClientRole,
        db=get_db,
        prefix='client_role',
        dependencies=[Depends(get_current_active_user)]
    ))
    
    
    app.include_router(SQLAlchemyCRUDRouter(
        schema=UserBase,
        create_schema=UserBase,
        update_schema=UserBase,
        db_model=User,
        db=get_db,
        prefix='user',
        dependencies=[Depends(get_current_active_user)]
    ))
    
    app.include_router(SQLAlchemyCRUDRouter(
        schema=GroupWithUsers,
        create_schema=GroupBase,
        update_schema=GroupBase,
        db_model=Group,
        db=get_db,
        prefix='group',
        dependencies=[Depends(get_current_active_user)]
    ))

    app.include_router(SQLAlchemyCRUDRouter(
        schema=GetDagWithRuns,
        create_schema=DagCreate,
        update_schema=DagUpdate,
        db_model=Dag,
        db=get_db,
        prefix='dag',
        dependencies=[Depends(get_current_active_user)]
        
    ))

    app.include_router(SQLAlchemyCRUDRouter(
        schema=DagRun,
        create_schema=DagRunCreate,
        update_schema=DagRunUpdate,
        db_model=DagRun,
        db=get_db,
        prefix='dag_run',
        dependencies=[Depends(get_current_active_user)]
    ))


    app.include_router(SQLAlchemyCRUDRouter(
        schema=DagTask,
        create_schema=DagTaskCreate,
        update_schema=DagTaskUpdate,
        db_model=DagTask,
        db=get_db,
        prefix='dag_task',
        dependencies=[Depends(get_current_active_user)]
    ))


    app.include_router(SQLAlchemyCRUDRouter(
        schema=DagTaskRun,
        create_schema=DagTaskRunCreate,
        update_schema=DagTaskRunUpdate,
        db_model=DagTaskRun,
        db=get_db,
        prefix='dag_task_run',
        dependencies=[Depends(get_current_active_user)]
    ))

    app.include_router(SQLAlchemyCRUDRouter(
        schema=ContactUpdate,
        create_schema=ContactCreate,
        update_schema=ContactUpdate,
        db_model=Contact,
        db=get_db,
        prefix='contact',
        dependencies=[Depends(get_current_active_user)]
    ))


    app.include_router(SQLAlchemyCRUDRouter(
        schema=Category,
        create_schema=CategoryCreate,
        update_schema=CategoryUpdate,
        db_model=Category,
        db=get_db,
        prefix='category',
        dependencies=[Depends(get_current_active_user)]
    ))


    app.include_router(SQLAlchemyCRUDRouter(
        schema=Attachment,
        create_schema=AttachmentCreate,
        update_schema=AttachmentUpdate,
        db_model=Attachment,
        db=get_db,
        prefix='attachment',
        dependencies=[Depends(get_current_active_user)]
    ))


    app.include_router(SQLAlchemyCRUDRouter(
        schema=MailServer,
        create_schema=MailServerCreate,
        update_schema=MailServerUpdate,
        db_model=MailServer,
        db=get_db,
        prefix='mailserver',
        dependencies=[Depends(get_current_active_user)]
    ))

    app.include_router(SQLAlchemyCRUDRouter(
        schema=Mailbox,
        create_schema=MailboxCreate,
        update_schema=MailboxUpdate,
        db_model=Mailbox,
        db=get_db,
        prefix='mailbox',
        dependencies=[Depends(get_current_active_user)]
    ))


