

from typing import Literal
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlmodel import Session
from auth import  get_current_active_user
from appmodels.airflow.dag import Dag, DagCreate
from appmodels.access_control.user import User
from sqlalchemy.exc import IntegrityError

from ebling.src.db import get_db

class DagNotify(BaseModel):
    dag_id: str
    state: Literal["started", "pending", "running", "success", "failed"]


framework_router = APIRouter()

@framework_router.get("/users/me/", response_model=Dag)
async def read_users_me(current_user: Dag = Depends(get_current_active_user)):
    return current_user


@framework_router.get("/users/me/items/")
async def read_own_items(current_user: Dag = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

@framework_router.post("/register_dag/")
def notif_dag(dag_notif: DagNotify,  current_user: User = Depends(get_current_active_user), session: Session = Depends(get_db)):
    if current_user.groups:
        print(current_user)
        dag_id:str
        try:
            dag = Dag(**request_dag.dict())
        except IntegrityError:
            dag: Dag = session.query(Dag).filter_by(dag_id=request_dag.dag_id).one()
        print(dag)

       
        
        



