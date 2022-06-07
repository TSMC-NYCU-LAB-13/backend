
from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    id: int
    title: str
    content: str
    url: str
    time: datetime
    keyword: str
    emotional_value: Optional[float] = None
    created_at: datetime

    class Config:
        orm_mode = True
