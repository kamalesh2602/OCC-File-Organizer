install:
	pip install -r requirements.txt

lint:
	flake8 .

test:
	pytest

docker-build:
	docker build -t file-organizer .

docker-run:
	docker run --rm file-organizer