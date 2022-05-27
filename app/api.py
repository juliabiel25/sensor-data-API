from fastapi import FastAPI, Depends
from .routers import humidity_temperature, co2, movement, users, background, oauth2_token
from .sql_app import models
from .sql_app.database import engine
from . import constants
from os import system
from os.path import join


# make sure the database is created by running the db setup script
# run the database_setup script
system(join(constants.__ROOT__, "sqlite_db", "database_setup.py"))


# global dependencies:
# app = FastAPI(dependencies=[Depends(get_query_token())])
models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# include all endpoint routers in the app instance
app.include_router(users.router)
app.include_router(humidity_temperature.router)
app.include_router(co2.router)
app.include_router(movement.router)
app.include_router(background.router)
app.include_router(oauth2_token.router)