FROM python:3.12-slim AS fr-base-backend

RUN apt-get update -q -y
RUN apt-get install -q -y --no-install-recommends --no-install-suggests \
    build-essential \
    gcc \
    python3-dev \
    libpq-dev

# Configure Poetry
ENV POETRY_VERSION=1.2.0
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# poetry
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip3 install -U pip setuptools \
    && $POETRY_VENV/bin/pip3 install poetry==${POETRY_VERSION}
ENV PATH="${PATH}:${POETRY_VENV}/bin"

WORKDIR /backend
COPY pyproject.toml ./
COPY poetry.lock ./

RUN poetry update
RUN poetry install


FROM fr-base-backend as fr-backend

WORKDIR /backend
COPY . .

CMD poetry run python3 manage.py migrate --no-input
CMD poetry run python3 manage.py collectstatic --no-input

EXPOSE 8000
ENTRYPOINT poetry run gunicorn server.asgi:application --config gunicorn_conf.py
