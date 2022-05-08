from contextlib import contextmanager
from sqlmodel import Session        
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging
import os

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.DEBUG)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
DB_URI = os.getenv("DB_URI", sqlite_url)

if "sqlite" in DB_URI:
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}

engine = create_engine(DB_URI, echo=True)

def get_db():
    session = Session(engine)
    try: 
        yield session
        session.commit()
    finally:
        session.close()
    
