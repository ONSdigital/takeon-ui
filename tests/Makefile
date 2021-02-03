docker-build:
	docker build -t bdd-tests .

set-url:
	export TAKEON_URL
	export COGNITO_USER_POOL
	echo $(TAKEON_URL)
	echo $(COGNITO_USER_POOL)

docker-compose:
	docker-compose up -d

docker-run: set-url docker-build
	docker run -e AWS_ACCESS_KEY_ID=$(AWS_ACCESS_KEY_ID) -e AWS_SECRET_ACCESS_KEY=$(AWS_SECRET_ACCESS_KEY) -e AWS_SESSION_TOKEN=$(AWS_SESSION_TOKEN)  -e TAKEON_URL='$(TAKEON_URL)' -e COGNITO_USER_POOL='$(COGNITO_USER_POOL)' -ti -w /code/acceptance-tests/ bdd-tests

