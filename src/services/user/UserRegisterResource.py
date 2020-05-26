from flask_restful import Resource
from services.AbstractResource import AbstractResource 
import hashlib


class UserRegisterResource(Resource, AbstractResource):
    def __init__(self):
        pass

    def get(self):
        user = self.get_single_param('user')
        password = self.get_single_param('password')

        encripted_password = hashlib.md5(password.encode('utf-8'))

        try:
            self.insert_user(user, encripted_password)
        except:
            print("Erro ao inserir usuário")

        return "user:" + user + ", password:" + str(encripted_password) 

    
    def insert_user (self, user, encripted_password):
        # get connection with database
        # execute insertion query
        # return status        
        pass