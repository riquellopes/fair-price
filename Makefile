.SILENT:
DJANGO=.venv/bin/python manage.py

up:
	docker-compose stop
	docker-compose up

build:
	docker-compose stop
	docker-compose build

migrate:
	docker-compose stop
	docker-compose run --rm options manage.py migrate

createsuperuser:
	docker-compose stop
	docker-compose run --rm options manage.py createsuperuser

makemigrations:
	docker-compose stop
	docker-compose run --rm options manage.py makemigrations

loaddata:
	docker-compose stop
	docker-compose run --rm options manage.py loaddata db.json

clean:
	find . -name "*.pyc" -exec rm -rf {} \;

debug:
	${DJANGO} runserver