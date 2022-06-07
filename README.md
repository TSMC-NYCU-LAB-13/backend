# Backend

## Install Library
```bash
pip install -r requirements.txt
```

## Run
```bash
python main.py
```

## Test
```bash
pytest

# run test coverage
py.test --cov=./ tests/
```

## API Document
- GET /api/statistics
    - Request Parameters
        - keywords: `list`
            - ex: ['tsmc', 'aa']
        - limit: `int` (幾周的資料)
            - ex: 5
    - Response
        ```
        [
            {
                "keyword": "tsmc",
                "data": [
                    {
                        "start_at": "2022-06-06T00:00:00",
                        "value_avg": 6.1,
                        "count": 3
                    },
                    {
                        "start_at": "2022-05-30T00:00:00",
                        "value_avg": 0.0,
                        "count": 0
                    },
                    {
                        "start_at": "2022-05-23T00:00:00",
                        "value_avg": 0.0,
                        "count": 0
                    },
                    {
                        "start_at": "2022-05-16T00:00:00",
                        "value_avg": 0.0,
                        "count": 0
                    },
                    {
                        "start_at": "2022-05-09T00:00:00",
                        "value_avg": 0.0,
                        "count": 0
                    }
                ]
            },
            {
                "keyword": "aa",
                "data": [
                    {
                        "start_at": "2022-06-06T00:00:00",
                        "value_avg": 12.5,
                        "count": 1
                    },
                    {
                        "start_at": "2022-05-30T00:00:00",
                        "value_avg": 0.0,
                        "count": 0
                    },
                    {
                        "start_at": "2022-05-23T00:00:00",
                        "value_avg": 0.0,
                        "count": 0
                    },
                    {
                        "start_at": "2022-05-16T00:00:00",
                        "value_avg": 0.0,
                        "count": 0
                    },
                    {
                        "start_at": "2022-05-09T00:00:00",
                        "value_avg": 0.0,
                        "count": 0
                    }
                ]
            }
        ]
        ```
- GET /api/articles
    - Request Parameters
        - keyword: `string`
            - ex: tsmc
        - start: `datetime`
            - ex: 2022-06-05T00:00:00
        - end: `datetime`
            - ex: 2022-06-08T00:00:00
    - Response
        ```
        [
            {
                "title": "tt",
                "url": "ttt",
                "keyword": "tsmc",
                "created_at": "2022-06-07T14:14:55",
                "time": "2022-06-07T14:14:47",
                "id": 2,
                "content": "werwrwe",
                "emotional_value": 3.3
            },
            {
                "title": "123",
                "url": "httpss://",
                "keyword": "tsmc",
                "created_at": "2022-06-06T23:28:53",
                "time": "2022-06-06T23:28:53",
                "id": 10,
                "content": "123",
                "emotional_value": 5.0
            },
            {
                "title": "test",
                "url": "https://",
                "keyword": "tsmc",
                "created_at": "2022-06-06T23:28:53",
                "time": "2022-06-06T23:28:42",
                "id": 1,
                "content": "tsdjflkwjkrwlekfjc,klsdjl",
                "emotional_value": 10.0
            }
        ]
        ```
- GET /api/keywords
    - Response
        ```
        {
            "keywords": [
                "test",
                "tsmc"
            ]
        }
        ```
- GET /api/db_status
    - Response
        - status: 200
        ```
        {
            "db_status": true
        }
        ```
        - status: 500
        ```
        {
            "detail": "Database Connect Error."
        }
        ```