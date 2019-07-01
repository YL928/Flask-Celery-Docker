from flask_restful import Resource
from flask import request
from . import api
from app.tasks import long_task
class HelloWorld(Resource):
    def get(self):
        r = long_task.apply_async()
        return {"msg": r.id}
    
class Check(Resource):
    def get(self):
        tid = request.args.get("id")
        print(tid)
        r = long_task.AsyncResult(tid)
        if r.status == 'SUCCESS':
            return {"msg":r.get()}
        return {"msg": r.status}
api.add_resource(HelloWorld, '/longtask')
api.add_resource(Check, '/status')