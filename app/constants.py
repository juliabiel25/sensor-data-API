from os.path import dirname
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

__ROOT__ = dirname(dirname(__file__))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "fakehashedsecret"
    },
    "alice": {
        "username": "alice",
        "email": "alice@example.com",
        "password": "fakehashedsecret2",
    },
}