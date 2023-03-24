FROM python:3.10-buster

RUN apt-get -y update; apt-get -y install curl sudo postgresql-client libpq-dev

RUN useradd -rm -s /bin/bash -g root -G sudo -u 1001 --no-log-init app
USER app
RUN mkdir /home/app/backend-flask
WORKDIR /home/app/backend-flask

COPY --chown=app:root requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY --chown=app:root . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]
