import os
from fastapi import FastAPI, Depends, HTTPException, Query
import uvicorn
from sqlalchemy.orm import Session
from typing import List
from dotenv import load_dotenv
from datetime import datetime

import crud, utils
from database import SessionLocal

load_dotenv()
app = FastAPI()

APP_URL   = os.getenv('APP_URL')
APP_PORT  = int(os.getenv('APP_PORT'))
APP_DEBUG = os.getenv('APP_DEBUG')

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/api/statistics')
def get_statistics(db: Session = Depends(get_db), keywords: List[str] = Query(None), limit: int = 10):
    response = []

    for keyword in keywords:
        articles = crud.get_articles(db, keyword, None, None)

        response.append({
            'keyword': keyword,
            'data': utils.get_statictic(articles, limit)
        })

    return response


@app.get('/api/articles')
def get_articles(db: Session = Depends(get_db), keyword: str = None, start: datetime = None, end: datetime = None):
    return crud.get_articles(db, keyword, start, end)


@app.get('/api/keywords')
def get_keywords(db: Session = Depends(get_db)):
    return {
        "keywords": crud.get_keywords(db)
    }


@app.get('/api/db_status')
def check_db_status(db: Session = Depends(get_db)):
    try:
        crud.get_all(db)
    except Exception:
        raise HTTPException(status_code=500, detail="Database Connect Error.")

    return {
        "db_status": True
    }


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=APP_URL, port=APP_PORT, reload=True, debug=APP_DEBUG) 
