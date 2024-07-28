.PHONY: run test install install-dev show-structure help

help:
	@echo "Available targets:"
	@echo "  install        : Install dependencies for production"
	@echo "  install-dev    : Install dependencies for development"
	@echo "  run            : Run project"
	@echo "  run            : Run project in debug mode"
	@echo "  test           : Run test suite"
	@echo "  format         : Format code"
	@echo "  tree           : Show project directory structure as tree"
	@echo "  help           : Display this help message"

install:
	poetry install --without dev

install-dev:
	poetry install && poetry run pre-commit install

run:
	export PYTHONPATH=$PYTHONPATH:$(pwd) && poetry run python src/main.py

dev:
	export PYTHONPATH=$PYTHONPATH:$(pwd) && poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload --log-level debug

test:
	poetry run pytest .

format:
	poetry run pre-commit run --all-files

build:
	docker build -t f-lab-python-backend-example:latest .

tree:
	tree -a -I '__pycache__|*.pyc|*.pyo|.pytest_cache|.venv|.git|.idea|__init__.py'
