from Config import Config
from OauthToken import OauthToken

class Api:
    def __init__(self):
        # Lista de tokens de usuários logados. 
        # Pode haver tokens vencidos
        self.authentication_list = []

        # Configurações de conexão com o banco.
        self.config = None

        # Lista de endpoints dinâmicos. São carregados do arquivo e/ou 
        # cadastrados por usuário. Por enquanto, apenas do arquivo.
        self.dynamic_endpoints = []


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

        # ...

        print("API is running!")