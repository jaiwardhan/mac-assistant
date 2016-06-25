# =====================================================================
# Utility to run shell commands on the system. Shell commands
# are run with the help of subprocess module.
# Able to handle commands in the form of a sting or a list with
# command arguments.
# Returns the data obtained
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

import subprocess


class SubprocessCall:

    # module to get back data from a subprocess call
    # @params: a list - command and options/switches for the command
    def subprocess_call_getdata(self, command_list, shell_mode):
        data = subprocess.Popen(command_list, stdout=subprocess.PIPE, shell=shell_mode).stdout.readlines()
        return data
