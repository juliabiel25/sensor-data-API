#
#   FastAPI uses pydantic models ("schemas") to send or receive data of a predefined format
#
from pydantic import BaseModel
from datetime import datetime


# common attributes for both creating and displaying data
class MovementBase(BaseModel):
    date_time: datetime


# a class used so that pydantic can read data other than simple python dictionaries
# (for example ORM models returned by db.query() - a sqlalchemy datatype)
# This allows to pass this class as a response_model argument in the API path operations
class MovementDetector(MovementBase):
    id: int

    class Config:
        orm_mode = True

class ShowMovement(MovementBase):

    class Config:
        orm_mode = True
