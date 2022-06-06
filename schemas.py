
from datetime import datetime
from pydantic import BaseModel


class Article(BaseModel):
    id: int
    title: str
    content: str
    url: str
    time: datetime
    keyword: str
    emotional_value: float
    created_at: datetime

    class Config:
        orm_mode = True
