class ErrorManager:

    def __init__(self):
        print "DEBUG_INIT: Initialized error manager"

    def error_respond(self, error, base_handler):
        base_handler.response_handler.respond_world("Sorry. That was an error")