from flask import Response
from werkzeug.exceptions import HTTPException

class MissingParamRequest(HTTPException):
    def __init__(self):
        self.message = "The request is missing a parameter." 
        self.code = 422