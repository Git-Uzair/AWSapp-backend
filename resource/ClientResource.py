import sys

sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database/wrapper")
from bson.objectid import ObjectId
from flask_restful import Resource, reqparse
from flask import jsonify
from ClientDataManager import ClientDataManager
from flask_jwt_extended import jwt_required, get_jwt_identity



class Client(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.db = ClientDataManager()
    @jwt_required
    def get(self, id):
        id = ObjectId(id)
        client = self.db.getClient(id)
       
        if client:
            client[0]["_id"] = str(client[0]["_id"])
            client[0]["updated_by"] = str(client[0]["updated_by"])
            client[0]["created_by"] = str(client[0]["created_by"])
            response = jsonify(client[0])
            response.status_code = 200
            return response
        else:
            response = jsonify("")
            response.status_code = 404
            return response
    @jwt_required
    def put(self, id):
        id = ObjectId(id)
        self.parser.add_argument("name", type=str)
        self.parser.add_argument("default_region", type=str)
        self.parser.add_argument("aws_access_key_id", type=str)
        self.parser.add_argument("aws_secret_access_key", type=str)
        self.parser.add_argument("status", type=bool)
        self.parser.add_argument("deleted", type=bool)

        client = self.parser.parse_args()
        client = self.db.updateClient(id, client)
        if client:
            response = jsonify({"_id": client})
            response.status_code = 201
            return response
        else:
            response = jsonify("")
            response.status_code = 404
            return response
    @jwt_required
    def post(self):
        self.parser.add_argument("name", type=str)
        self.parser.add_argument("default_region", type=str)
        self.parser.add_argument("aws_access_key_id", type=str)
        self.parser.add_argument("aws_secret_access_key", type=str)
        self.parser.add_argument("status", type=bool)
        self.parser.add_argument("created_by", type=str)
        self.parser.add_argument("deleted", type=bool)

        client = self.parser.parse_args()
        client = self.db.addClient(client)
        if client == "Duplicate":
            response = jsonify(client)
            response.status_code = 406
            return response

        response = jsonify({"_id": client})
        response.status_code = 201
        return response
    @jwt_required
    def delete(self, id):
        id = ObjectId(id)
        deleted = self.db.deleteClient(id)
        if deleted == "deleted":
            response = jsonify({"_id": str(id)})
            response.status_code = 200
            return response
