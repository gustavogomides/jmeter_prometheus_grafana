import json
import logging
import os

from flask import Flask
from api.config import config_by_name


def create_app(config_name):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object(config_by_name[config_name])

        app.wsgi_app = PrefixMiddleware(
            app.wsgi_app, prefix='/matmul'
        )

        return app


class PrefixMiddleware(object):

    def __init__(self, app, prefix=''):
        self.app = app
        self.prefix = prefix

    def __call__(self, environ, start_response):

        if environ['PATH_INFO'].startswith(self.prefix):
            environ['PATH_INFO'] = environ['PATH_INFO'][len(self.prefix):]
            environ['SCRIPT_NAME'] = self.prefix
            return self.app(environ, start_response)
        else:
            start_response('404', [('Content-Type', 'text/plain')])
            return ["This url does not belong to the app.".encode()]
