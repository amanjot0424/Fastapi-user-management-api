from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas import LoginRequest
from models import User
from database import get_db
from security import (
    verify_password,
    create_access_token,
    get_current_user,
)
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/login")
def login(user: LoginRequest, db: Session=Depends(get_db)):
    db_user=db.query(User).filter(User.email==user.email).first()
    if db_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    if not verify_password(user.password,db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    token=create_access_token({"sub":db_user.email})
    return {
        "access_token":token,
        "token_type": "bearer"
    }

@router.get("/profile")
def get_current(current_user: str=Depends(get_current_user)):
    return{
        "email":current_user
    }