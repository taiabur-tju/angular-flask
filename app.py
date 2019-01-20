from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
# from json import dumps
from flask_jsonpify import jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
    return jsonify({'db-data':"hello data"})

class Employees(Resource):
    def get(self):
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]}

class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id':1, 'name':'Balram'}}
        return jsonify(result)

class alldata(Resource):
    def get(self):
        app.config["MONGO_URI"] = "mongodb://localhost:27017/lms"
        mongo = PyMongo(app)
        # online_users = mongo.db.users.update({"name":"siqiChen"},{'title':"teacher Bigdata","name":"siqiChen"})
        online_users = mongo.db.users.find()
        # print({"dbdata":online_users})
        # return jsonify({"dbdata":app.config})
        result =''.join(map(str, online_users))
        return jsonify(result)


class create_user(Resource):
    def get(insertdata):
        app.config["MONGO_URI"] = "mongodb://localhost:27017/lms"
        mongo = PyMongo(app)
        # online_users = mongo.db.users.update({"name":"siqiChen"},{'title':"teacher Bigdata","name":"siqiChen"})
        online_users = mongo.db.users.insert(insertdata)
        # print({"dbdata":online_users})
        # return jsonify({"dbdata":app.config})
        result =''.join(map(str, online_users))
        return jsonify(result)

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3
api.add_resource(alldata, '/db') # Route_3
api.add_resource(create_user, '/create_user') # Route_3


if __name__ == '__main__':
   app.run(port=5002)