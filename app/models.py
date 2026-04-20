from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    username =Column(String(50), unique=True, index=True, nullable = False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default = True)


