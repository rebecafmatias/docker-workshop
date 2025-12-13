FROM python:3.12.1-slim

RUN pip install pandas pyarrow

WORKDIR /code
COPY pipeline.py .

ENTRYPOINT ["python","pipeline.py","12"]