import os
import pytest
import sqlalchemy
from dotenv import load_dotenv
from src.database import Base
from main import app, get_db

load_dotenv()

DB_CONNECTION = os.getenv('DB_CONNECTION')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_DATABASE = f"{os.getenv('DB_DATABASE')}_test"

SQLALCHEMY_DB_URL = f"{DB_CONNECTION}+{DB_CONNECTION}connector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

engine = sqlalchemy.create_engine(SQLALCHEMY_DB_URL)
TestingSessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db
