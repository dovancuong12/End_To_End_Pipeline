.PHONY: help install dev-install test lint format clean docker-up docker-down

# Project management commands for End-to-End Pipeline

help:
	@echo "Available commands:"
	@echo "  install        - Install the package in development mode"
	@echo "  dev-install    - Install the package with development dependencies"
	@echo "  test           - Run tests"
	@echo "  lint           - Run code linting"
	@echo "  format         - Format code with black"
	@echo "  clean          - Clean temporary files"
	@echo "  docker-up      - Start all services with docker-compose"
	@echo "  docker-down    - Stop all services"

install:
	pip install -e .

dev-install:
	pip install -e ".[dev]"

test:
	pytest -v --cov=src/

lint:
	flake8 src/
	mypy src/

format:
	black src/

clean:
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name __pycache__ -delete
	find . -name "*.pyc" -delete

docker-up:
	docker-compose -f infra/docker-compose.yml up -d

docker-down:
	docker-compose -f infra/docker-compose.yml down

# Pipeline execution commands
run-batch:
	python -m spark.batch.batch_job

run-streaming:
	python -m spark.streaming.streaming_job

run-airflow:
	airflow standalone

run-sdk-demo:
	python -c "from sdk.your_sdk import client; print('SDK imported successfully')"