from xxlimited import Str

from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    priority: str | None = "media"

class TaskOut(BaseModel):
    id: int
    tittle: str
    description: str | None = None
    completed: bool
    priority: str
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True

class TaskUpdate(BaseModel):
    tittle: Str | None = None
    description: str | None = None
    completed: bool | None = None
    priority: str | None = None

