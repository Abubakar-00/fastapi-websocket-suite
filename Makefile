.PHONY: server client test lint format docker-build docker-up

server:
	uvicorn server.main:app --reload --host 0.0.0.0 --port 8000

client:
	python -m client.main

test:
	python -m pytest tests/

lint:
	flake8 .
	black --check .
	isort --check-only .

format:
	black .
	isort .

docker-build:
	docker-compose build

docker-up:
	docker-compose up
