from fastapi import Depends, Response, status, HTTPException, APIRouter
from ..sql_app import models
from ..sql_app.schemas import movement
from sqlalchemy.orm import Session
from typing import List, Optional
from ..dependencies import get_db
from ..constants import oauth2_scheme

# initialize API router with all the common traits
router = APIRouter(
    prefix="/movement",
    tags=["movement detector"],
    responses={
        404: {
            "description": "Not found"
        }
    }
)


# add a "movement detected!" record (for testing purposes)
@router.post("/", status_code=status.HTTP_201_CREATED)
def add_new_record(request: movement.MovementBase,
                   token: str = Depends(oauth2_scheme),
                   db: Session = Depends(get_db)):
    new_record = models.MovementDetector(
        date_time=request.date_time)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return {"New record": new_record}


# show all "movement detected" dates
@router.get("/", response_model=List[movement.ShowMovement])
def get_records(token: str = Depends(oauth2_scheme),
                limit: Optional[int] = None,
                db: Session = Depends(get_db)):
    movement_model = models.MovementDetector
    query_res = db.query(movement_model)
    res_len = query_res.count()
    if limit:
        return query_res.order_by(movement_model.date_time).offset(res_len-limit).limit(limit).all()
    else:
        return query_res.order_by(movement_model.date_time).all()









