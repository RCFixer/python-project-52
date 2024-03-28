.PHONY: install dev lint start build

install:
	poetry install

dev:
	python manage.py runserver

lint:
	poetry run flake8 task_manager
