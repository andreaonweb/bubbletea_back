from sqlalchemy import Column, String, Boolean, Date, DateTime
from sqlalchemy.sql import func
from app.db.connection import Base

class UserORM(Base):
    __tablename__ = "users"

    id         = Column(String(128), primary_key=True)  
    name       = Column(String(100), nullable=False)
    surname    = Column(String(100), nullable=False)
    email      = Column(String(200), nullable=False)
    birth_date = Column(Date, nullable=True)
    active     = Column(Boolean, default=True)
    notifications = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())