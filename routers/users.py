from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import User
from security import hash_password
from schemas import UserCreate, UserResponse, MessageResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("",response_model=UserResponse)
def create_user(user:UserCreate,db:Session=Depends(get_db)):
    new_user=User(
        name=user.name,
        age=user.age,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print("ID:", new_user.id)
    return new_user

@router.get("", response_model=list[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user

@router.put("/{user_id}",response_model=UserResponse)
def update_user(user_id:int,user:UserCreate, db: Session=Depends(get_db)):
    filter_user=db.query(User).filter(User.id==user_id).first()
    if filter_user is None:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    
    filter_user.name=user.name
    filter_user.age=user.age
    filter_user.email=user.email
    filter_user.password=hash_password(user.password)
    
    db.commit()
    db.refresh(filter_user)
    return filter_user

@router.delete("/{user_id}",response_model=MessageResponse)
def drop_user(user_id:int, db: Session=Depends(get_db)):
    filter_user=db.query(User).filter(User.id==user_id).first()
    if filter_user is None:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    db.delete(filter_user)
    db.commit()
    return {
        "message":"user deleted successfully"
    }