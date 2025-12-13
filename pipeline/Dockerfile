FROM python:3.12.1-slim

WORKDIR /code

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

COPY pipeline.py .

ENTRYPOINT ["python","pipeline.py","12"]