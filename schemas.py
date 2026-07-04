from fastapi import FastAPI
from pydantic import BaseModel
class UserCreate(BaseModel):
    name: str
    age: int
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str

class MessageResponse(BaseModel):
    message: str

class LoginRequest(BaseModel):
    email: str
    password: str