import os
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

DB_CONNECTION = os.getenv('DB_CONNECTION')
DB_USERNAME   = os.getenv('DB_USERNAME')
DB_PASSWORD   = os.getenv('DB_PASSWORD')
DB_HOST       = os.getenv('DB_HOST')
DB_PORT       = os.getenv('DB_PORT')
DB_DATABASE   = os.getenv('DB_DATABASE')

SQLALCHEMY_DB_URL = f"{DB_CONNECTION}+{DB_CONNECTION}connector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
Engine = sqlalchemy.create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base = declarative_base()

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
