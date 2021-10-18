import sys
sys.path.insert(1, "e:/Data/Internships/Gosaas/Project/Backend/database")
from Connection import Connection

class LoginDataManager:
    def __init__(self):
        self.__db = Connection.getConnection()
    
    def authenticate(self,user):
        User = self.__db['users']
        User = User.find_one({'email':user['email'],"password": user['password']})
        if User!= None:
            User['_id']= str(User['_id'])
            User['created_by']= str(User['created_by'])
            User['updated_by']= str(User['updated_by'])
            user=[User]
            return user

        return list()
        
        


        
        

