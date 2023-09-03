FROM python:3.11.4 AS base-backend

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

CMD [ "poetry", "run", "python", "manage.py", "migrate"]
CMD [ "poetry", "run", "python", "manage.py", "collectstatic", "--no-input"]
COPY . /backend

FROM base-backend as dev-backend

EXPOSE 8000

CMD [ "poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
