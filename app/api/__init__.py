from flask import Blueprint
from flask_restful import Api, fields

# bind blueprints with unique path
api_blueprint = Blueprint("api", __name__, url_prefix='/api')

api = Api(api_blueprint)

from . import survey