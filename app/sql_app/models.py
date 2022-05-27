#
#   this is were all sqlalchemy ORM models (mapping the database tables) are defined
#
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)

    # # table relationships
    # hum_temp_sensor = relationship("HumidityTemperatureSensor", back_populates="owner")


class HumidityTemperatureSensor(Base):
    __tablename__ = "humidity_temperature"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime)
    humidity = Column(Float)
    temperature = Column(Float)

    # # foreign key
    # user_id = Column(Integer, ForeignKey("users.id"))
    #
    # # table relationship
    # owner = relationship("User", back_populates="hum_temp_sensor")

class CO2Sensor(Base):
    __tablename__ = "mq7"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime)
    co_value = Column(Float)
    co_warning = Column(Integer)

class MovementDetector(Base):
    __tablename__ = "movement"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime)
