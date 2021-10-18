import sys

sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database")
from Connection import Connection


class UsersDataManager:
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