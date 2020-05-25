from flask import request
from exceptions.MissingParamRequest import MissingParamRequest

class AbstractResource:
    def __init__(self):
        pass
    

    def get_single_param (self, param_name):
        raw_param = request.args.getlist(param_name)
        
        if len(raw_param) > 0:
            return raw_param[0]

        # Retornar algo para informar que falta parâmetro
        # 422 http status
        raise MissingParamRequest() # Não está sendo tratado pela api