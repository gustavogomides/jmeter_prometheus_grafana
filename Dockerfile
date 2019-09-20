FROM python:3.6.8-jessie

ENV APP_DIR /usr/src/app

RUN	apt-get update && \
    apt-get install -y nano && \
    pip3 install --upgrade pip && \
    rm -rf /var/cache/apk/*

COPY . ${APP_DIR}
WORKDIR ${APP_DIR}

EXPOSE 8000

RUN pip3 install -r requirements.txt

ENTRYPOINT gunicorn --workers 4 --worker-class="egg:meinheld#gunicorn_worker" --timeout 900 --bind 0.0.0.0:8000 manage:app
