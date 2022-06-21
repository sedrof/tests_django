web_container = web
db_container = helpcenter_postgres
db_name = helpcenter_postgres
db_user= bigcommand_helpcenter


mm:
	docker-compose exec $(web_container) python manage.py makemigrations

m:
	docker-compose exec $(web_container) python manage.py migrate

s:
	docker-compose exec $(web_container) python manage.py shell

dbshell:
	docker-compose exec $(web_container) python manage.py dbshell

t:
	docker-compose exec $(web_container) python manage.py test

tp:
	docker-compose exec $(web_container) python manage.py test --parallel

b:
	docker-compose exec $(web_container) bash

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

count:
	docker-compose exec $(web_container) bash -c 'git ls-files | xargs wc -l'

logs:
	docker-compose logs $(web_container)

psql:
	docker-compose exec $(db_container) psql -d $(db_name) -U $(db_user)
