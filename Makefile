init:
	python3 -m venv venv
	source ./venv/bin/activate
	
install:
	pip install -r requirements.txt 

test:
	python -m unittest tests/test_breakfast.py

build:
	python setup.py sdist