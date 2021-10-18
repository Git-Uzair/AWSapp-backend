import boto3
from flask import Flask, jsonify
from flask_restful import Api, Resource
from bson.objectid import ObjectId
from resource.UserResource import User
from resource.ClientResource import Client
from resource.LoginResource import Login
from resource.ClientsResource import Clients
from resource.UsersResource import Users
from resource.Ec2Resource import Ec2
from flask_web_log import Log
from flask_cors import CORS, cross_origin
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = '!@#$giberrish123'
cors = CORS(app)
app.config['CORS_HEADERS']='Content-Type'
app.config['LOG_TYPE']='JSON'
app.config['LOG_LOCATION'] = 'logs'
app.config["CORS_SUPPORTS_CREDENTIALS"]=True

api = Api(app)
jtw = JWTManager(app)
Log(app)

api.add_resource(Login, "/login")

api.add_resource(
    Client,
    "/client/<string:id>",
    "/client",
    "/client/<string:id>",
    "/client/<string:id>",
)

api.add_resource(Clients, "/clients")
api.add_resource(Users, "/user/getall")

api.add_resource(
    User,
    "/user/<string:id>",
    "/user",
    "/user/<string:id>",
    "/user/<string:id>",
)
api.add_resource(Ec2, "/ec2")



if __name__ == "__main__":
    app.run(debug=True)
