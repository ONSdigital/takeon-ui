FROM python:3.8

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable


# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


# set display port to avoid crash and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null



RUN mkdir /code
WORKDIR /code

COPY .  /code/
COPY /acceptance-tests/  /code/acceptance-tests/




RUN pip install --upgrade pip
RUN pip install -r /code/requirements_local.txt


#CMD ["python", "./app.py"]




#ENTRYPOINT ["wrapper.sh"]
CMD behave -f plain --no-capture
#CMD /bin/sh wrapper.sh
# for running for docker file run the command  docker run -ti -w /code/acceptance-tests/ bddsel1
#run this command for up the yml file docker-compose up -d
# for running in  docker compose docker run  --network="host" -ti -w /code/acceptance-tests/  bdd-selenium-python_test
# docker run  --network="host" -v /Users/Mohamf/bdd-selenium-python/acceptance-tests/docker_results:/code/docker_results  -ti -w /code/acceptance-tests/  bdd-dkr-img
#to enter inside docker image -  docker run -ti --entrypoint=/bin/sh bdd-docker-img1
