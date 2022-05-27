#
#   FastAPI uses pydantic models ("schemas") to send or receive data of a predefined format
#
from pydantic import BaseModel
from datetime import datetime


# common attributes for both creating and displaying data
class CO2Base(BaseModel):
    date_time: datetime
    co_value: float
    co_warning: int


# a class used so that pydantic can read data other than simple python dictionaries
# (for example ORM models returned by db.query() - a sqlalchemy datatype)
# This allows to pass this class as a response_model argument in the API path operations
class CO2Sensor(CO2Base):
    id: int

    class Config:
        orm_mode = True


class CO2Add(CO2Base):
    pass


class ShowCO2(CO2Base):

    class Config:
        orm_mode = True
