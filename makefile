setup:
	pre-commit install
	pip install -r requirements.txt

test:
	pytest --cov
	flake8

format:
	black main.py account.py test_account.py
