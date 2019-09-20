import os

from flask import request, current_app
from flask_restplus import Resource
from datetime import datetime
from api.quadratic_equation import ns as api
from api.utils.response import return_response
from api.quadratic_equation.business import CalculatorBusiness


@api.route('/')
class Solve(Resource):

    def post(self):
        try:
            return return_response(
                CalculatorBusiness.solve_quadratic_equation(request.json),
                201
            )
        except Exception as e:
            print(str(e))
            return return_response({
                "success": False,
                "message": 'ERRO'
            }, 500)
