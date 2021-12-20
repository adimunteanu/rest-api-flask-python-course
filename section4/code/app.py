from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = [

]


class Item(Resource):
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'item': None}, 404

    def post(self, name):
        item = {
            'name': name,
            'price': 12
        }
        items.append(item)
        return item, 201

    def put(self, name):
        pass

    def delete(self, name):
        pass


api.add_resource(Item, '/item/<string:name>')

app.run(port=5000)
