import os
from fastapi import FastAPI, Depends
import uvicorn
from sqlalchemy.orm import Session
from typing import List
from dotenv import load_dotenv

import crud, schemas
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


@app.get('/articles', response_model=List[schemas.Article])
def get_articles(db: Session = Depends(get_db)):
    return crud.get_articles(db)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=APP_URL, port=APP_PORT, reload=True, debug=APP_DEBUG) 
