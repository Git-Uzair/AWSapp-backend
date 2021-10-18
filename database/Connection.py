import pymongo
from pymongo import MongoClient


class Connection(object):
    __db = None

    @classmethod
    def getConnection(self):
        if self.__db is None:
            print("***********Connecting***********")
            self.__db = MongoClient("MONGODB CONNECTION URL GOES HERE", w=0)
            self.__db = self.__db["awscontroller"]
            print("***********DB connection successful***********")
        return self.__db
        

    