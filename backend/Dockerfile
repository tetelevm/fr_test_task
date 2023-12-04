FROM python:3.11.6 AS base-backend

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
RUN poetry update
RUN poetry install


FROM base-backend as dev-backend

EXPOSE 8000

COPY . /backend
ENTRYPOINT ["sh", "/backend/entrypoint.sh"]
