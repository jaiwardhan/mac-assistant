from openManager import OpenManager
from ErrorManager import ErrorManager
from ResponseManager import ResponseManager

class BaseMachine:
    open_manager = OpenManager()
    error_handler = ErrorManager()
    response_manager = ResponseManager()
    ERR_COMM_UNDERFLOW = -1
    ERR_COMM_OVERFLOW = -2
    ERR_COMM_ILLEGAL = -3

    # Default value: ILLEGAL
    exit_code = "-3OOO-3"

    def __init__(self):
        # init all super
        print "init all super"

