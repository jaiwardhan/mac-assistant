# from BaseMachine import BaseMachine
from ResponseManager import ResponseManager

class ErrorManager():

    response_manager = ResponseManager()
    def error_respond(self, error):
        print self.__module__
        self.response_manager.respond_world("Sorry. That was an error")