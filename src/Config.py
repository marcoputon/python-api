import os
import json 


'''
Arquivo de configurações.

Os atributos de conexão são criados dinamicamente. Estão definidos apenas 
para não dar erro na IDE, mas não é necessário.

Todo - Criptografar senhas.
'''
class Config:
    def __init__(self):
        # Conection
        self.ip = None
        self.port = None
        self.user = None
        self.password = None
        self.database = None

        # Config paths
        self.CONNECTION_NAME = "/connection.config"

        self.HOME_DIR = self.get_home_dir()
        self.CONNECTION_CONFIG_DIR = self.HOME_DIR + self.CONNECTION_NAME
        
        # Load
        self.load_config()


    ''' 
    Carrega o arquivo de configurações de conexão e cria os atributos da 
    classe dinamicamente.
    
    Se o arquivo não existir, o mesmo será criado com valores padrão e 
    a aplicação será encerrada.
    '''
    def load_config (self):
        try:
            with open(self.CONNECTION_CONFIG_DIR) as file:
                data = file.read().replace('\n', '')
        except FileNotFoundError:
            default_config = (
                '{\n' + 
                    '\t"ip": "localhost", \n' + 
                    '\t"port": "5432", \n' +
                    '\t"user": "postgres", \n' +
                    '\t"password": "postgres", \n' + 
                    '\t"database": "teste" \n' +
                '}'
            )
            file = open(self.CONNECTION_CONFIG_DIR, "w+")
            file.write(default_config)
            file.close()
            print("ERROR: \n\t\tArquivo " + self.CONNECTION_CONFIG_DIR + " não encontrado. Arquivo padrão criado.")
            exit(0)

        self.__dict__ = json.loads(data)

    
    '''
    Retorna o diretório de configurações da aplicação.
    Precisa da variável de ambiente API_HOME.
    '''
    def get_home_dir (self):
        path = os.environ.get('API_HOME')
        if path == None:
            print("ERROR: \n\t\tA variável de ambiente 'API_HOME' não existe.")
            exit(0)
        return path


    '''
    Para questões de debug.
    Não usar em release.
    '''
    def __str__(self):
        s = ""
        
        for attr, value in self.__dict__.items():
            s += attr + ": " + value + "\n"

        return s