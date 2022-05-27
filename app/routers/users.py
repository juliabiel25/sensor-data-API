from fastapi import Depends, status, APIRouter
from ..sql_app import models
from ..sql_app.schemas import user
from sqlalchemy.orm import Session
from ..dependencies import get_db
from typing import List
from ..sql_app.schemas.user import UserBase
from ..authentication import get_password_hash


router = APIRouter(
    prefix="/users",
    tags=["users"],
    # dependencies=[Depends(get_token_header)],    # wymóg autoryzacji dla wszystkich endpointów w tym module
    responses={
        404: {
            "description": "Not found"
        }
    })


# create a new user account
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(request: user.UserCreate,
                db: Session = Depends(get_db)):
    new_user = models.User(email=request.email, password=get_password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"New added user": new_user}


# delete a user account
@router.delete("/{user_id}")
def delete_user_by_ID(user_id: int,
                      db: Session = Depends(get_db), status_code=200):
    db.query(models.User).filter(models.User.id == user_id).delete(synchronize_session=False)
    db.commit()
    return {"message": "User deleted"}


# show all user accounts
@router.get("/", response_model=List[user.ShowUser])
def get_users(skip: int = 0, limit: int = 100,
              db: Session = Depends(get_db)):
    print(db.query(models.User).offset(skip).limit(limit).all())
    return db.query(models.User).offset(skip).limit(limit).all()






### TESTOWANIE LOGOWANIA
#
#
# @router.get("/current")
# async def get_user(current_user: UserBase = Depends(get_current_active_user)):
#     return current_user
