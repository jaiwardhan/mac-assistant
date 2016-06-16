# Utility to run subprocess commands.
# Contains modules required to execute
# list & string commands to subprocess.
# Returns the data obtained
# @author: Jaiwardhan Swarnakar

import subprocess


class SubprocessCall:

    # module to get back data from a subprocess call
    # @params: a list - command and options/switches for the command
    def subprocess_call_getdata(self, command_list, shell_mode):
        data = subprocess.Popen(command_list, stdout=subprocess.PIPE, shell=shell_mode).stdout.readlines()
        return data
