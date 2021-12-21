-include .env

# target: createdb - Create the initial DB
.PHONY: createdb
createdb:
	docker exec -it stock_service_db createdb -U postgres stock_service

# target: createsuperuser - Create a super user account
.PHONY: createsuperuser
createsuperuser:
	./manage.py createsuperuser

# target: deps - Install project dependencies
.PHONY: deps
deps:
	pip install --upgrade pip
	pip install -r requirements.txt

# target: makemigrations - Create migration files
.PHONY: makemigrations
makemigrations:
	./manage.py makemigrations

# target: migrate - Execute the migrations
# and migrate database models
.PHONY: migrate
migrate:
	./manage.py migrate

# target: removedb -Remove the database container and
# its data volume
.PHONY: removedb
removedb: stopdb
	docker volume rm stock_service_data

# target: reset_db - Reset the database
.PHONY: reset_db
reset_db:
	./manage.py reset_db

# target: reset_schema - Reset the database schema
.PHONY: reset_schema
reset_schema:
	./manage.py reset_schema

# target: setup - Install the pre-commit requirement
.PHONY: setup
setup:
	pre-commit install

# target: start - Run server (Default)
.PHONY: start
start:
	./manage.py runserver

# target: startdb - Start the database container
.PHONY: startdb
startdb:
	docker run -d --name stock_service_db \
      -v stock_service_data:/var/lib/postgresql/data \
      -p 5432:5432 \
      -e POSTGRES_HOST_AUTH_METHOD=trust \
      postgres:12

# target: stopdb - Stop the database container
.PHONY: stopdb
stopdb:
	docker stop stock_service_db
	docker rm stock_service_db

# target: schema - Create/Update the graphql schema file "data/schema.graphql"
.PHONY: schema
schema:
	python manage.py graphql_schema

# Tests
# target: test - Run tests
.PHONY: test
test:
	pytest
