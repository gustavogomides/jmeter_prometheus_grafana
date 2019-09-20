from flask import Blueprint
from flask_restplus import Api

from api.quadratic_equation.controllers.quadratic_equation import api as quadratic_equation_ns

blueprint = Blueprint('quadratic_equation', __name__)

api = Api(blueprint, doc=False)

api.add_namespace(quadratic_equation_ns)
