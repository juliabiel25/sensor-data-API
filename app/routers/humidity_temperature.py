from fastapi import Depends, Response, status, HTTPException, APIRouter
from ..sql_app import models
from ..sql_app.schemas import hum_temp_sensor
from sqlalchemy.orm import Session
from typing import List, Optional
from ..dependencies import get_db
from ..constants import oauth2_scheme

# initialize API router with all the common traits
router = APIRouter(
    prefix="/hum-temp",
    tags=["humidity & temperature sensor"],
    responses={
        404: {
            "description": "Not found"
        }
    }
)


# add a humidity & temperature record (for testing purposes)
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_new_record(request: hum_temp_sensor.HumTempAdd,
                   token: str = Depends(oauth2_scheme),
                   db: Session = Depends(get_db)):
    new_record = models.HumidityTemperatureSensor(
        date_time=request.date_time,
        humidity=request.humidity,
        temperature=request.temperature)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return {"New record": new_record}


# show all humidity & temperature values
@router.get("/", response_model=List[hum_temp_sensor.ShowHumTemp])
def get_records(token: str = Depends(oauth2_scheme),
                limit: Optional[int] = None,
                db: Session = Depends(get_db)):
    hum_temp_model = models.HumidityTemperatureSensor
    query_res = db.query(hum_temp_model)
    res_len = query_res.count()
    if limit:
        return query_res.order_by(hum_temp_model.date_time).offset(res_len-limit).limit(limit).all()
    else:
        return query_res.order_by(hum_temp_model.date_time).all()









