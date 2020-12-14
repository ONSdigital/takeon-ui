docker-build:
	docker build -t bdd-tests .

set-url:
	export TAKEON_URL
	echo $(TAKEON_URL)

docker-compose:
	docker-compose up -d

docker-run: set-url docker-build
	docker run  -e TAKEON_URL='$(TAKEON_URL)' -ti -w /code/acceptance-tests/ bdd-tests
