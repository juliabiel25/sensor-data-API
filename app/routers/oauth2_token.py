from fastapi.security import OAuth2PasswordRequestForm

from fastapi import Depends, status, APIRouter, HTTPException
from ..sql_app import models
from ..sql_app.schemas import user
from sqlalchemy.orm import Session
from ..dependencies import get_db
from typing import List
from ..sql_app.schemas.user import UserBase, UserCreate
from ..constants import fake_users_db
from ..authentication import *

router = APIRouter(
    prefix="/token",
    tags=["authentication token"],
    responses={
        404: {
            "description": "Not found"
        }
    })

@router.post("/", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
