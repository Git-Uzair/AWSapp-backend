import sys
from bson.objectid import ObjectId
from datetime import datetime
from pymongo import ReturnDocument

sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database")
from Connection import Connection


class ClientDataManager:
    def __init__(self):
        self.__db = Connection.getConnection()

    def getClient(self, _id):
        try:
            Client = self.__db["clients"]
            result = Client.find({"_id": _id})
            return list(result)
        except Exception as e:
            print(e)

    def updateClient(self, id, client):
        try:
            Client = self.__db["clients"]
            
            Client.find_one_and_update(
                {"_id": id},
                {
                    "$set": {
                        "name": client["name"],
                        "default_region": client["default_region"],
                        "aws_access_key_id": client["aws_access_key_id"],
                        "aws_secret_access_key": client["aws_secret_access_key"],
                        "status": client["status"],
                        "deleted": client["deleted"]
                    }
                },
            )
            return str(id)
        except Exception as e:
            print(e)

    def addClient(self, client):
        try:
            Client = self.__db["clients"]
            client["created"] = datetime.now()
            client["updated_by"] = ""
            client["deleted"]=False
            client["created_by"] = ObjectId(client["created_by"])
            if Client.find({"name": client["name"]}).count() > 0:
                return "Duplicate"

            client = Client.insert_one(client)

            return str(client.inserted_id)
        except Exception as e:
            print(e)

    def getAllClients(self):
        try:
            Client = self.__db["clients"]
            result = Client.find()
            result = list(result)
            clients = []
            for client in result:
                client["_id"] = str(client["_id"])
                clients.append(client)

            return clients
        except Exception as e:
            print(e)
    
    def deleteClient(self, id):
        try:
            Client = self.__db["clients"]
            Client = Client.find_one_and_delete({"_id": id})
            return "deleted"

        except Exception as e:
            print(e)
