import sys

sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database/wrapper")
from bson.objectid import ObjectId
from flask_restful import Resource, reqparse, request
from flask import jsonify
from Ec2DataManager import Ec2DataManager
from flask_jwt_extended import jwt_required, get_jwt_identity



class Ec2(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.__db = Ec2DataManager()
    @jwt_required
    def get(self):
        args = request.args
        instance_list = self.__db.getAllInstances(args["client_name"], args["region"])
        if instance_list == None:
            response = jsonify(instance_list)
            response.status_code = 404
            return response
        else:
            response = jsonify(instance_list)
            response.status_code = 200
            return response
    @jwt_required
    def post(self):
        self.parser.add_argument("client_name", type=str)
        self.parser.add_argument("instance_id", type=str)
        self.parser.add_argument("action", type=str)
        self.parser.add_argument("region", type=str)
        ec2 = self.parser.parse_args()

        if ec2["action"] == "stop":
            response = self.__db.stopInstance(
                ec2["instance_id"], ec2["client_name"], ec2["region"]
            )
            if response == ec2["instance_id"]:
                response = jsonify(response)
                response.status_code = 200
                return response
            else:
                response = jsonify(response)
                response.status_code = 404
                return response
        elif ec2['action']=='start':
            response = self.__db.startInstance(
                ec2["instance_id"], ec2["client_name"], ec2["region"]
            )
            if response == ec2["instance_id"]:
                response = jsonify(response)
                response.status_code = 200
                return response
            else:
                response = jsonify(response)
                response.status_code = 404
                return response
        elif ec2['action']=='restart':
            response =  self.__db.restartInstance(
                ec2['instance_id'],ec2['client_name'],ec2['region']
            )
            if response == ec2['instance_id']:
                response = jsonify(response)
                response.status_code = 200
                return response
            else:
                response = jsonify(response)
                response.status_code = 404
                return response
