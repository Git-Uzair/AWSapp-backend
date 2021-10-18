import sys

sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database/wrapper")
from bson.objectid import ObjectId
from flask_restful import Resource, reqparse
from flask import jsonify
from UserDataManager import UserDataManager


class User(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.db = UserDataManager()

    def get(self, id):
        id = ObjectId(id)
        user = self.db.getUser(id)
        if user:
            user[0]["_id"] = str(user[0]["_id"])
            user[0]["updated_by"] = str(user[0]["updated_by"])
            user[0]["created_by"] = str(user[0]["created_by"])
            response = jsonify(user[0])
            response.status_code = 200
            return response
        else:
            return "Not found", 404

    def put(self, id):
        id = ObjectId(id)
        self.parser.add_argument("first", type=str)
        self.parser.add_argument("last", type=str)
        self.parser.add_argument("email", type=str)
        self.parser.add_argument("password", type=str)
        self.parser.add_argument("status", type=str)
        self.parser.add_argument("updated_by", type=str)

        user = self.parser.parse_args()
        user = self.db.updateUser(id, user)
        if user:
            response = jsonify(user)
            response.status_code = 200
            return response
        else:
            return "Not found", 404

    def post(self):
        self.parser.add_argument("first", type=str)
        self.parser.add_argument("last", type=str)
        self.parser.add_argument("email", type=str)
        self.parser.add_argument("password", type=str)
        self.parser.add_argument("status", type=str)
        self.parser.add_argument("created_by", type=str)
        user = self.parser.parse_args()
        user = self.db.addUser(user)
        response = jsonify(user)
        response.status_code = 201
        return response

    def delete(self, id):
        id = ObjectId(id)
        deleted = self.db.deleteUser(id)
        response = jsonify(deleted)
        response.status_code = 200
        return response