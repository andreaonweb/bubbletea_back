from sqlalchemy import Column, Integer, String, Float, Boolean
from pydantic import BaseModel, Field
from typing import Optional
from app.db.connection import Base

class BubbleTeaORM(Base):
    __tablename__ = "bubbleteas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    temperature = Column(String(10), nullable=False)
    price = Column(Float, nullable=False)
    active = Column(Boolean, default=True)


class BubbleTea(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=2, max_length=100)
    temperature: str = Field(..., pattern="^(hot|cold|both)$")
    price: float = Field(..., gt=0)
    active: bool = True

    class Config:
        from_attributes = True