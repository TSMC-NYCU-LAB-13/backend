import sys, os
sys.path.append(os.getcwd())
from fastapi.testclient import TestClient
import datetime
import string, random
from main import app

client = TestClient(app)


def get_random_string():
    return ''.join(random.choice(string.ascii_letters) for x in range(10))


def create_fake_item(keyword: None, time=None, emotional_value=None):
    data = {
        "title": "pytest",
        "url": f"https://{get_random_string()}",
        "keyword": "pytest" if keyword == None else keyword,
        "time": "2022-01-01T00:00:00" if time == None else time,
        "content": get_random_string(),
        "emotional_value": 10 if emotional_value == None else emotional_value,
    }
    return client.post("/api/articles", json=data).json()


def test_get_statistics(test_db):
    create_fake_item(keyword="tsmc", time="2022-06-06T00:00:00")
    create_fake_item(keyword="tsmc", time="2022-06-07T00:00:00")
    create_fake_item(keyword="tsmc", time="2022-06-08T00:00:00")

    params = {
        "keywords": "tsmc",
        "limit": 10,
    }
    response = client.get("/api/statistics", params=params)
    assert response.status_code == 200
    assert response.json()[0]["keyword"] == "tsmc"
    assert len(response.json()[0]["data"]) == 10


def test_articles(test_db):
    create_fake_item(keyword="tsmc", time="2022-06-06T00:00:00")
    create_fake_item(keyword="tsmc", time="2022-06-07T00:00:00")
    create_fake_item(keyword="tsmc", time="2022-06-08T00:00:00")

    params = {
        "keyword": "tsmc"
    }
    response = client.get("/api/articles", params=params)
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_articles_keyword(test_db):
    create_fake_item(keyword="tsmc", time="2022-06-06T00:00:00")
    create_fake_item(keyword="tsmc", time="2022-06-07T00:00:00")
    create_fake_item(keyword="tsmcc", time="2022-06-08T00:00:00")

    params = {
        "keyword": "tsmc",
        "start": datetime.datetime(2022, 6, 5, 0, 0, 0),
        "end": datetime.datetime(2022, 6, 9, 0, 0, 0)
    }
    response = client.get("/api/articles", params=params)
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_articles_time_range(test_db):
    create_fake_item(keyword="tsmc", time="2022-06-06T00:00:00")
    create_fake_item(keyword="tsmc", time="2022-06-07T00:00:00")
    create_fake_item(keyword="tsmc", time="2022-07-07T00:00:00")

    params = {
        "keyword": "tsmc",
        "start": datetime.datetime(2022, 6, 5, 0, 0, 0),
        "end": datetime.datetime(2022, 6, 9, 0, 0, 0)
    }
    response = client.get("/api/articles", params=params)
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_keywords(test_db):
    fake_data1 = create_fake_item(keyword="test1")

    response = client.get("/api/keywords")
    assert response.status_code == 200
    assert response.json() == {
        "keywords": [fake_data1['keyword']]
    }


def test_keywords_duplicate(test_db):
    create_fake_item(keyword="abc")
    create_fake_item(keyword="xyz")
    create_fake_item(keyword="abc")

    response = client.get("/api/keywords")
    assert response.status_code == 200
    assert len(response.json()['keywords']) == 2
