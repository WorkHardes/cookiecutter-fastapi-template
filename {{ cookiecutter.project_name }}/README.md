# Some API

## Usage

Install the dependencies:

```bash
poetry shell
poetry install
```

Run the app:

```bash
make start-server
```

### OpenAPI documentation

After server start:

- swagger docs - `http://localhost:8000/docs`
- redoc - `http://localhost:8000/redoc`

---

## Containers

Build and run docker container in interactive mode

```bash
make build-docker-image
make run-docker-container
```
