init:
	python3 -m venv ./venv

install:
	pip install -r requirements.txt 

test:
	python -m unittest -v tests/test_breakfast.py
	python -m unittest -v tests/test_food.py

build:
	python setup.py sdist