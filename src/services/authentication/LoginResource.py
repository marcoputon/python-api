from flask_restful import Resource
from services.AbstractResource import AbstractResource 
import hashlib
import time


class LoginResource(Resource, AbstractResource):
    def __init__(self):
        pass

    def get(self):
        user = self.get_single_param('user')
        password = self.get_single_param('password')

        encripted_password = hashlib.md5(password.encode('utf-8'))
        
        if self.login(user, encripted_password):
            token = self.generate_token(user + password + str(time.time()))
            # todo - Adicionar na lista de tokens

        return "user:" + user + ", password:" + password 

    
    def login (self, user, encripted_password):
        return True


    def generate_token (self, key):
        return hashlib.md5(key.encode('utf-8'))