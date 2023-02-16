FROM python:3.11-slim-buster

ENV TERM=linux \
    TERMINFO=/etc/terminfo \
    # pip
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry
    POETRY_VERSION=1.3.2 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR="/var/cache/pypoetry" \
    PATH="$PATH:/root/.local/bin"

WORKDIR /usr/src/some_api/

# Project initialization
COPY app /usr/src/some_api/app
COPY pyproject.toml /usr/src/some_api/

RUN pip install poetry==${POETRY_VERSION} \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root --no-dev

CMD ["gunicorn", "app.main:app", "--bind", "0.0.0.0:4000", "--reuse-port", "-k", "app.core.CustomUvicornWorker"]
