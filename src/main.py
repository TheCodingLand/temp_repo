from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routers.custom_routers import include_custom_routers
from routers.crud_routers import include_crud_routers
from routers.users_router import users_router
from routers.rapidoc_router import rapidoc_router


#from db import engine
app = FastAPI(   
    title="Ebling",
    description="Backtrading tracker system, with stategy management",
    version="0.0.1",
    terms_of_service="https://trading.next-in-tech.com/terms/",
    contact={
        "name": "Julien Le Bourg",
        "url": "https://trading.next-in-tech.com/creator/",
        "email": "julien.lebourg@ctg.lu",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

def create_db_and_tables():
    pass
    #SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

origins = [
    "https://next-in-tech.fr",
    "http://localhost:3001",
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

include_crud_routers(app)
include_custom_routers(app)
app.include_router(users_router)
app.include_router(rapidoc_router)

if __name__ == "__main__":
    #import asyncio
    #asyncio.run(create_mailserver())
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000, log_level="info")