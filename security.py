from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta, UTC
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os
load_dotenv()


#adding hashed password and verify password funtion:
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

#adding jwt tokens
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("Algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(UTC) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

#adding authorization bearer
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str=Depends(oauth2_scheme)):
    try:
        payload= jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        email= payload.get("sub")

        if email is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        
        return email
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
print("SECRET_KEY:", repr(SECRET_KEY))
print("ALGORITHM:", repr(ALGORITHM))
print("EXP:", repr(ACCESS_TOKEN_EXPIRE_MINUTES))