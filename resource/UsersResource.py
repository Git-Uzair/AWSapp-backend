import sys
sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database/wrapper")
from bson.objectid import ObjectId
from flask_restful import Resource, reqparse
from flask import jsonify
from UsersDataManager import UsersDataManager
from flask_jwt_extended import jwt_required, get_jwt_identity


class Users(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.__db = UsersDataManager()
    @jwt_required
    def get(self):
        clients = self.__db.getAllUsers()
        response = jsonify(clients)
        response.status_code = 200
        return response
