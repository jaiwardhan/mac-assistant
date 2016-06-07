import sys
import os


class ExecManager():

    def exec_command(self,command):
        print "DEBUG: (exectuing in execMgr): " + command
        os.system(command)
