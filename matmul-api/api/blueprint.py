from flask import Blueprint
from flask_restplus import Api

from api.matmul.controllers.matmul import api as matmul_ns

blueprint = Blueprint('matmul', __name__)

api = Api(blueprint, doc=False)

api.add_namespace(matmul_ns)
