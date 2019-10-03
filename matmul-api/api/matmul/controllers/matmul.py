import os

from flask import request, current_app
from flask_restplus import Resource
from api.utils.response import return_response
import numpy as np
from api.matmul import ns as api


@api.route('/')
class MatMulResource(Resource):

    def post(self):
        try:
            qty = int(request.json.get('shape', 1000)) or 1000
            if qty > 10000:
                return return_response({
                    "success": False,
                    "message": 'Shape deve ser menor que 1000000'
                }, 400)
            a = np.random.rand(qty, qty)
            np.matmul(a, a)
            return return_response({
                "success": True,
                "message": 'OK'
            }, 201)
        except Exception as e:
            print(str(e))
            return return_response({
                "success": False,
                "message": 'ERRO'
            }, 500)
