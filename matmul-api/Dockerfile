FROM python:3.6.8-jessie

ENV APP_DIR /usr/src/app

RUN	apt-get update && \
    apt-get install -y curl nano

COPY . ${APP_DIR}
WORKDIR ${APP_DIR}

EXPOSE 8000

RUN pip3 install -r requirements.txt

ENTRYPOINT gunicorn --workers 4 --worker-class="egg:meinheld#gunicorn_worker" --access-logfile=- --timeout 900 --bind 0.0.0.0:8000 manage:app