docker-build:
	docker build -t bdd-tests .

docker-compose:
	docker-compose up -d

docker-run:
	export UI_URL=TAKEON_URL
	echo $(UI_URL)
	docker run  -e TAKEON_URL='$(UI_URL)'  -v $(CURDIR)/acceptance-tests/docker_results:/code/docker_results  -ti -w /code/acceptance-tests/ bdd-tests
