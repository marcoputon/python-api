from flask_restful import Resource
from services.AbstractResource import AbstractResource 
import hashlib


class UserExistsResource(Resource, AbstractResource):
    def get(self):
        user = self.get_single_param('user')
        
        try:
            return self.user_exists(user)
        except:
            print("Erro ao verificar se o usuario existe.")

        
    def user_exists (self, user):
        # get database connection
        # execute query
        # return status
        return False