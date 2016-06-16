# @author: Jaiwardhan Swarnakar
from execManager import ExecManager
from ErrorManager import ErrorManager
from ResponseManager import ResponseManager
from utils.InstalledApps import InstalledApps

class BaseMachine:
    exec_handler = ExecManager()
    error_handler = ErrorManager()
    response_handler = ResponseManager()

    apps_installed = None
    running_apps = None
    running_apps_path = None

    ERR_COMM_UNDERFLOW = -1
    ERR_COMM_OVERFLOW = -2
    ERR_COMM_ILLEGAL = -3

    # Default value: ILLEGAL
    exit_code = "-3OOO-3"

    def __init__(self):
        # init all super
        print "init all super"
        self.apps_installed = (InstalledApps()).get_installed_apps()

