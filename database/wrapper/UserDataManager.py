import sys

sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database")
from Connection import Connection
from datetime import datetime
from bson.objectid import ObjectId
from pymongo import ReturnDocument


class UserDataManager:
    def __init__(self):
        self.__db = Connection.getConnection()

    def getAllUsers(self):
        try:
            User = self.__db["users"]
            result = User.find()
            result = list(result)
            users = []
            for user in result:
                user["_id"] = str(user["_id"])
                user['created_by']= str(user['created_by'])
                user['updated_by']= str(user['updated_by'])
                users.append(user)

            return users
        except Exception as e:
            print(e)

    def getUser(self, _id):
        try:
            User = self.__db["users"]
            result = User.find({"_id": _id})
            users = []
            for user in result:
                user["_id"] = str(user["_id"])
                user['created_by']= str(user['created_by'])
                user['updated_by']= str(user['updated_by'])
                users.append(user)
            return list(users)
        except Exception as e:
            print(e)

    def addUser(self, user):
        try:
            User = self.__db["users"]
            user["created"] = datetime.now()
            user["updated_by"] = ""
            user["created_by"] = ObjectId(user["created_by"])
            user = User.insert_one(user)

            return str(user.inserted_id)
        except Exception as e:
            print(e)

    def updateUser(self, id, user):
        try:
            User = self.__db["users"]
            User = User.find_one_and_update(
                {"_id": id},
                {
                    "$set": {
                        "first": user["first"],
                        "last": user["last"],
                        "email": user["email"],
                        "password": user["password"],
                        "status": user["status"],
                        "updated_by": ObjectId(user["updated_by"]),
                    }
                },
                return_document=ReturnDocument.AFTER,
            )

            return str(id)
        except Exception as e:
            print(e)

    def deleteUser(self, id):
        try:
            User = self.__db["users"]
            User.find_one_and_delete({"_id": id})

            return str(id)

        except Exception as e:
            print(e)
