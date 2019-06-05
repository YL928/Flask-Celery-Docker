from flask_restful import Resource
from . import api

class HelloWorld(Resource):
    def get(self):
        return {"msg": "ssss"}
api.add_resource(HelloWorld, '/rest')