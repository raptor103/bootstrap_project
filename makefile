setup:
	pre-commit install
	pip install -r requirements.txt

test:
	pytest --cov src
	flake8 src

format:
	black src/
