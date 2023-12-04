#!/bin/sh

poetry run python3 manage.py migrate --no-input
poetry run python3 manage.py collectstatic --no-input
poetry run gunicorn server.asgi:application --config gunicorn_conf.py
