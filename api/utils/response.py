# -*- coding: utf-8 -*-
from flask import Response, json


def return_response(data, status_code):
    return Response(json.dumps(data), status_code, content_type='application/json')
