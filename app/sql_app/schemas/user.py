#
#   FastAPI uses pydantic models ("schemas") to send or receive data of a predefined format
#
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from .hum_temp_sensor import HumTempBase


# common attributes for both creating and displaying data
class UserBase(BaseModel):
    email: str


# additional arguments for creating a user
class UserCreate(UserBase):
    password: str

# additional line that allows us to use this as an sqlalchemy response body formatter
class ShowUser(UserBase):
    password: str
    class Config:
        orm_mode = True
