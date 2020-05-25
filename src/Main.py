from Server import Server
from flask import Flask, request
from flask_restful import Resource, Api
from Errors import errors

flask_app = Flask(__name__)
flask_api = Api(flask_app, errors=errors)


'''
Antes de iniciar a api, certificar que os arquivos de configuração
estão preenchidos corretamente.
'''
def main ():
    server = Server(flask_app, flask_api)
    server.run()


if __name__ == "__main__":
    main()