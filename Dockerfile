FROM python:3.12

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./
RUN poetry install --no-dev

COPY . .

EXPOSE 8000
