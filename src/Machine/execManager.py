# =====================================================================
# Manager to execute shell commands through OS system calls.
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

import os


class ExecManager:

    def __init__(self):
        print "DEBUG_INIT: initialized exec manager"

    # Module to execute os system call.
    # Takes the command to be executed in the form of
    # a string which is assumed to be a valid terminal command
    def exec_command(self, command):
        print "DEBUG: (exectuing in execMgr): " + command
        os.system(command)
