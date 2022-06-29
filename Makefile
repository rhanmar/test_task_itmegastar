build:
	docker-compose build

up:
	docker-compose up

down:
	docker-compose down

fill_db:
	docker-compose exec web python manage.py fill_db

migrate:
	docker-compose exec web python manage.py migrate

test:
	docker-compose exec web python manage.py test