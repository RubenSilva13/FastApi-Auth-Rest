from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    username =Column(String(50), unique=True, index=True, nullable = False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default = True)

class Task(Base):
    __tablename__ = "tasks"

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    completed   = Column(Boolean, default=False)
    priority    = Column(String(10), default="media")
    created_at  = Column(DateTime, default=datetime.utcnow)
    owner_id    = Column(Integer, ForeignKey("users.id"), nullable=False)

