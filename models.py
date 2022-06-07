from sqlalchemy import Column, Integer, FLOAT, TEXT, DATETIME, TIMESTAMP
from database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(TEXT)
    content = Column(TEXT)
    url = Column(TEXT, unique=True)
    time = Column(DATETIME)
    keyword = Column(TEXT, index=True)
    emotional_value = Column(FLOAT, nullable=True)
    created_at = Column(TIMESTAMP)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
