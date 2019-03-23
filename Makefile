init:
	python3 -m venv venv
	source ./venv/bin/activate
	
install:
	pip install -r requirements.txt 

test:
	nosetests tests