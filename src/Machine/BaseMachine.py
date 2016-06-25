# =====================================================================
# Base class to initialize all the managers and utilities.
# All references in to the "external" managers and the utilities should
# be made through the instance of this class.
# The objective of this structure is to make the data available
# and transparent throughout the application which makes life simple.
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

from execManager import ExecManager
from ErrorManager import ErrorManager
from ResponseManager import ResponseManager
from utils.InstalledApps import InstalledApps
from utils.CurrentActiveAppWindow import CurrentActiveAppWindow


class BaseMachine:

    # Initialize all managers
    exec_handler = ExecManager()
    error_handler = ErrorManager()
    response_handler = ResponseManager()

    # Initialize all util daemons
    current_active_window = CurrentActiveAppWindow()

    # Declarations of daemons that can be used upon
    # calls. This is to make sure that they are only
    # called when they are needed.
    apps_installed = None
    running_apps = None
    running_apps_path = None

    # Standard command error codes.
    ERR_COMM_UNDERFLOW = -1
    ERR_COMM_OVERFLOW = -2
    ERR_COMM_ILLEGAL = -3

    # Default value: ILLEGAL
    exit_code = "-3OOO-3"

    def __init__(self):

        # Init all.
        print "init all super"

        # Get a list of apps currently installed on the system.
        # TODO: this might not get updated when something is installed when the program is already running
        self.apps_installed = (InstalledApps()).get_installed_apps()

