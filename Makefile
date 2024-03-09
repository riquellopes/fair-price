.SILENT:
DJANGO=.venv/bin/python manage.py
PYTEST=.venv/bin/py.test

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
	${DJANGO} runserver 0.0.0.0:8000 --settings=fair_price.settings.local

calc_average_price:
	${DJANGO} calc_average_price

test:
	${PYTEST} -s -r a --color=yes