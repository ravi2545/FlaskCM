from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todo = {}

class Name(Resource):
    def get(self):
        return {'Name': 'Ravi Prasad'}


class TooDoo(Resource):
    def get(self, tid):
        return {tid: todo[tid]}
    
    def put(self, tid):
        todo[tid] = request.form['data']
        return {tid: todo[tid]}

    
api.add_resource(TooDoo, '/ravi/<string:tid>', endpoint='todo_ep')
api.add_resource(Name, '/', '/hello')


if __name__ == '__main__':
    app.run(debug=True)