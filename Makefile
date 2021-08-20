run_docker:
	@cp -p src/Pipfile docker/backend/
	@cp -p src/Pipfile.lock docker/backend/
	@cd docker && docker-compose --env-file ../src/.env up
	@rm docker/backend/Pipfile
	@rm docker/backend/Pipfile.lock

run_local:
	@cd docker && docker-compose --env-file ../src/.env up --no-start postgres
	@docker run --rm -d --env-file src/.env -p 5432:5432 postgres
	@docker/backend/wait_for_postgres.sh
	@cd src && python manage.py migrate && python manage,py runserver
