from flask_restful import Resource
from services.AbstractResource import AbstractResource 


class LoginResource(Resource, AbstractResource):
    def __init__(self):
        pass

    def get(self):
        user = self.get_single_param('user')
        password = self.get_single_param('password')

        return "user:" + user + ", password:" + password 