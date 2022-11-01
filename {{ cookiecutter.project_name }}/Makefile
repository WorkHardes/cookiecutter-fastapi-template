help:
	@echo "Commands:";
	@echo "lint: lint code in app folder with flake8 linter";
	@echo "init-pre-commit: init pre-commit in .git";
	@echo "pre-commit: runs pre-commit";
	@echo "start-server: starts server at host: '$(SERVER_HOST)' and port: '$(SERVER_PORT)'";
	@echo "build-docker-image: builds docker image with name '$(DOCKER_IMAGE_NAME)'";
	@echo "run-docker-container: runs docker container with name '$(DOCKER_IMAGE_NAME)'";

lint:
	flake8 ./app/

init-pre-commit:
	pre-commit install

pre-commit:
	pre-commit run --all-files

start-server:
	gunicorn app.main:app --bind $(SERVER_HOST):$(SERVER_PORT) --reuse-port -k app.core.CustomUvicornWorker

build-docker-image:
	TARGETPLATFORM=linux DOCKER_BUILDKIT=1 docker build -t $(DOCKER_IMAGE_NAME) -f $(DOCKERFILE_FILE_NAME) $(DOCKERFILE_PATH)

run-docker-container:
	docker run -p $(SERVER_PORT):$(SERVER_PORT)/tcp $(DOCKER_IMAGE_NAME)
