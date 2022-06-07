from sqlalchemy.orm import Session
from datetime import datetime

from models import Article


def get_all(db: Session):
    return db.query(Article).all()


def get_articles(db: Session, keyword: str, start: datetime, end: datetime):
    if (start and end):
        return db.query(Article).filter(
            Article.keyword == keyword,
            Article.emotional_value.isnot(None),
            start < Article.time,
            Article.time < end,
        ).order_by(
            Article.time.desc()
        ).all()

    return db.query(Article).filter(
        Article.keyword == keyword,
        Article.emotional_value.isnot(None)
    ).order_by(
        Article.time.desc()
    ).all()


def get_keywords(db: Session):
    articles = db.query(Article).all()
    keywords = [data.keyword for data in articles]
    return list(set(keywords))

