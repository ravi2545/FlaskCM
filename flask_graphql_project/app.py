# Imports
from typing import List
from flask import Flask
import graphene
from flask_graphql import GraphQLView
import psycopg2
from graphene import ObjectType, String, Field
from graphql import GraphQLError
import json
from flask import jsonify

# app initialization
app = Flask(__name__)
app.debug = True


# Models
class Category(ObjectType):
    name = String()

class Categories(ObjectType):
    getCategories = Field(Category)
    def resolve_getCategories(self, request):
        data = [{'name': 'kalyan'}, {'name': 'prasad'}]
        ks = jsonify(data)
        return data

# Schema Objects
class CategoryQuery(Categories, ObjectType):
    pass

class Query(CategoryQuery ,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)


# Routes
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True # for having the GraphiQL interface
    )
)



@app.route('/')
def index():
    return '<p> Hello World</p>'
if __name__ == '__main__':
     app.run()