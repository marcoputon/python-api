import os
import json 


'''
Arquivo de configurações.

Os atributos de conexão são criados dinamicamente. Estão definidos apenas 
para não dar erro na IDE, mas não é necessário.

Todo - Criptografar senhas 
'''
class Config:
    def __init__(self):
        # Conection
        self.ip = None
        self.port = None
        self.user = None
        self.password = None
        self.database = None

        # Config path
        self.HOME_DIR = self.get_home_dir()
        
        # Load
        self.load_config()


    ''' 
    Carrega o arquivo de configurações de conexão e cria os atributos da 
    classe dinamicamente
    '''
    def load_config (self):
        with open(self.HOME_DIR + "/connection.config") as file:
            data = file.read().replace('\n', '')

        self.__dict__ = json.loads(data)

    
    '''
    Retorna o diretódio de configurações da aplicação.
    Precisa da variável de ambiente API_HOME 
    '''
    def get_home_dir (self):
        return os.environ.get('API_HOME')


    '''
    Para questões de debug.
    Não usar em release.
    '''
    def __str__(self):
        s = ""
        
        for attr, value in self.__dict__.items():
            s += attr + ": " + value + "\n"

        return s