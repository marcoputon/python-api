from Config import Config
from OauthToken import OauthToken
from flask import Flask
from flask_restful import Resource

# Todo - Separar em outro arquivo
from services.authentication.LoginResource import LoginResource


class Server:
    def __init__(self, flask_app, flask_api):
        # Lista de tokens de usuários logados. 
        # Pode haver tokens vencidos
        self.authentication_list = []

        # Configurações de conexão com o banco.
        self.config = None

        # Lista de endpoints dinâmicos. São carregados do arquivo e/ou 
        # cadastrados por usuário. Por enquanto, apenas do arquivo.
        self.dynamic_endpoints = []

        # Aplicação flask. As requisções são feitas por ela. 
        self.flask_app = flask_app

        # Onde os endpoins são configurados
        self.flask_api = flask_api


    '''
    A api possui 3 métodos básicos: login, logout e isLoged.
    '''
    def login (self, user, password):
        pass

    def logout (self, token):
        pass

    def isLoged (self, token):
        return token in self.authentication_list


    '''
    Método para iniciar a API.
    Configurar a conexão antes de chamar.
    '''
    def run (self):
        print("API is starting...")

        print("\tGet connection configuration: ", end="")
        self.config = Config()
        print("DONE")
        
        print("\tCreating endpoints: ", end="")
        self.init_resources()
        print("DONE")

        self.flask_app.run()
        print("API is running!")


    # Todo - Separar em outro arquivo
    def init_resources (self):
        self.flask_api.add_resource(LoginResource, '/login')