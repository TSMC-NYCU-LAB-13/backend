from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class Article(BaseModel):
    title: str
    content: str
    url: str
    time: datetime
    keyword: str
    emotional_value: Optional[float] = None

    class Config:
        orm_mode = True
