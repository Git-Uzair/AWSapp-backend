import sys

sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database/wrapper")
from bson.objectid import ObjectId
from flask_restful import Resource, reqparse
from flask import jsonify
from ClientsDataManager import ClientsDataManager
from flask_jwt_extended import jwt_required, get_jwt_identity



class Clients(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.__db = ClientsDataManager()
    @jwt_required
    def get(self):
        clients = self.__db.getAllClients()
        response = jsonify({"clients":clients})
        response.status_code = 200
        return response
