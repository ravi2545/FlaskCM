from flask import *
from graphene import ObjectType, String
from flask_classful import FlaskView


app = Flask(__name__)


class TestView(FlaskView):

    class MyName(ObjectType):
        name = String()

        def resolve_MyName()

    def index(self):
    # http://localhost:5000/
        return "Ravi Prasad"

TestView.register(app,route_base = '/')


if __name__ == '__main__':
    app.run(debug=True)
    b = Rav()