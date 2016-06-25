# =====================================================================
# Manager to handle errors for illegal command usages.
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

class ErrorManager:

    def __init__(self):
        print "DEBUG_INIT: Initialized error manager"

    # Module to respond to the user that the command sent was
    # either illegal or not valid.
    # TODO: This could be used more effectively to handle errors later
    def error_respond(self, error, base_handler):
        base_handler.response_handler.respond_world("Sorry. That was an error")