install:
	pipenv install -r requirements.txt
lint:
	pipenv run flake8 .
test: lint
run:
	pipenv run python tictactoe.py