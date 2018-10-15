import Hybrid
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Crypto(Resource):
    def get(self, message):
        return {'decrypt': Hybrid.hybrid(message)}

api.add_resource(Crypto, '/crypto/<message>')

if __name__ == '__main__':
     app.run()