FROM python:3.10-slim
COPY . /backend
WORKDIR /backend
RUN apt-get update && \
    apt-get -yy install gcc libmariadb3 libmariadb-dev
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    pip install -r requirements.txt
# ENTRYPOINT ["/backend/entrypoint.sh"]
CMD ["uvicorn", "main:app"]