from fastapi import Depends, Response, status, HTTPException, APIRouter
from ..sql_app import models
from ..sql_app.schemas import co2_sensor
from sqlalchemy.orm import Session
from typing import List, Optional
from ..dependencies import get_db
from ..constants import oauth2_scheme

# initialize API router with all the common traits
router = APIRouter(
    prefix="/co2",
    tags=["CO2 sensor"],
    responses={
        404: {
            "description": "Not found"
        }
    }
)


# add a CO2 record (for testing purposes)
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_new_record(request: co2_sensor.CO2Add,
                   token: str = Depends(oauth2_scheme),
                   db: Session = Depends(get_db)):
    new_record = models.CO2Sensor(
        date_time=request.date_time,
        co_value=request.co_value,
        co_warning=request.co_warning)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return {"New record": new_record}


# show all CO2 values
@router.get("/", response_model=List[co2_sensor.ShowCO2])
def get_records(token: str = Depends(oauth2_scheme),
                limit: Optional[int] = None,
                db: Session = Depends(get_db)):
    co2_model = models.CO2Sensor
    query_res = db.query(co2_model)
    res_len = query_res.count()
    if limit:
        return query_res.order_by(co2_model.date_time).offset(res_len-limit).limit(limit).all()
    else:
        return query_res.order_by(co2_model.date_time).all()









