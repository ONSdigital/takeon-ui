docker-build:
	docker build -t bdd-tests .

docker-compose:
	docker-compose up -d

docker-run:
	#docker run -ti -w /code/acceptance-tests/ bdd-tests
#	docker run --name temp-container bdd-tests /bin/sh
#	docker cp temp-container:/code/acceptance-tests/docker_results /Users/Mohamf/takeon-ui/tests/acceptance-tests/docker_results
#	docker run -ti -w /code/acceptance-tests/ bdd-tests
#	docker cp temp-container:/code/acceptance-tests/docker_results /Users/Mohamf/takeon-ui/tests/acceptance-tests/docker_results

	docker run  --network="host" -v /Users/Mohamf/takeon-ui/tests/acceptance-tests/docker_results:/code/docker_results  -ti -w /code/acceptance-tests/ bdd-tests

check-img:
	docker run -ti --entrypoint=/bin/sh bdd-tests

