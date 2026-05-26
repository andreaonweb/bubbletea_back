from pydantic import BaseModel, Field
from typing import Optional

class BubbleTea(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=2, max_length=100)
    temperature: str = Field(..., pattern="^(hot|cold|both)$")
    price: float = Field(..., gt=0)
    active: bool = True