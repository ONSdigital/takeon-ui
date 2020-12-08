docker-build:
	docker build -t bdd-tests .

docker-compose:
	docker-compose up -d

docker-run:
	export TAKEON_URL
	echo $(TAKEON_URL)
	docker run  -e TAKEON_URL='$(TAKEON_URL)' -v $(CURDIR)/acceptance-tests/docker_results:/code/docker_results  -ti -w /code/acceptance-tests/ bdd-tests
