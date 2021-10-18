import sys

sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database/wrapper")
from bson.objectid import ObjectId
from flask_restful import Resource, reqparse
from flask import jsonify
from LoginDataManager import LoginDataManager
import datetime
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.db = LoginDataManager()

    def post(self):
        self.parser.add_argument("email", type=str)
        self.parser.add_argument("password", type=str)
        user = self.parser.parse_args()
        data = self.db.authenticate(user)
        if len(data) == 1:
            user = data[0]
            token = create_access_token(identity=user["email"])
            response = jsonify(
                {
                    "user": {"name": user["first"], "email": user["email"], "_id": user["_id"]},
                    "token": token,
                }
            )
            response.status_code = 200
            return response
        else:
            return "User Not Found", 404
