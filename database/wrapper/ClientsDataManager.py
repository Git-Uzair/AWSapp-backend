import sys
sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database")
from Connection import Connection


class ClientsDataManager:
    def __init__(self):
        self.__db = Connection.getConnection()

    def getAllClients(self):
        try:
            Client = self.__db["clients"]
            result = Client.find()
            result = list(result)
            clients = []
            for client in result:
                client["_id"] = str(client["_id"])
                client['updated_by']=str(client['updated_by'])
                client['created_by']=str(client['created_by'])
                clients.append(client)

            return clients
        except Exception as e:
            print(e)
