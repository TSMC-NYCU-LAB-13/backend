from sqlalchemy.orm import Session

import models


def get_articles(db: Session):
    return db.query(models.Article).all()
