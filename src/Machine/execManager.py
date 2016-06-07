import os


class ExecManager:

    def __init__(self):
        print "DEBUG_INIT: initialized exec manager"

    def exec_command(self,command):
        print "DEBUG: (exectuing in execMgr): " + command
        os.system(command)
