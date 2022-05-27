from .constants import pwd_context, oauth2_scheme
from .dependencies import get_db
from sqlalchemy.orm import Session
from fastapi import Depends
from jose import JWTError, jwt
from pydantic import BaseModel
from typing import Optional
from datetime import timedelta, datetime
from .sql_app import models
from .sql_app.schemas.user import UserCreate

SECRET_KEY = "6f5f15e214ff60b08156c816dafc583cd34e980c34325aac42c1c3bace0057bf"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db: Session,
             username: str):
    res = db.query(models.User.email, models.User.password).filter(models.User.email == username).one_or_none()
    if not res is None:
        res = dict(res)
        user = UserCreate(**res)
        print("found user:", res)
        return user
    return None

def authenticate_user(db: Session,
                      username: str,
                      password: str):
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(token_data.username)
    if user is None:
        raise credentials_exception
    return user
