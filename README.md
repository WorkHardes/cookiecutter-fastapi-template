# {{ cookiecutter.project_name }}

This repository contains a cookiecutter fastapi project template

## Project Structure

```
{{ cookiecutter.project_name }}/
|── app/
│   ├── __init__.py
|   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── errors/
│   │   │   ├── __init__.py
│   │   │   ├── http_error.py
│   │   │   └── validation_error.py
│   │   └── routers/
│   │       ├── __init__.py
│   │       ├── api.py
│   │       └── users.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config/
│   │   │   └── __init__.py
│   │   └── events/
│   │       └── __init__.py
│   ├── internal/
│   │   ├── __init__.py
│   │   └── admin.py
│   ├── models/
│   │   └── __init__.py
│   └── schemas/
│      ├── __init__.py
│      └── error.py
├── examples/
├── scripts/
├── tests/
├── .editorconfig
├──.flake8
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yaml
├── Dockerfile
├── Makefile
├── pyproject.toml
└── README.md
```
