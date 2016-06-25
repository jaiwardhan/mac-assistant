# =====================================================================
# Manager to close running application on the system.
# This manager relies on system calls, data from activity monitor and
# I have ensured that this doesn't affect any unexpected/trashy close.
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

from utils.RunningApps import RunningApps

class CloseManager:

    # General filter: Should be removed.
    filterRef = ["up", "the", "in", "for", "me", "please", "copy", "instance", "a", "of", "alright", "window"]

    def __init__(self):
        print "DEBUG_INIT: Initialized CloseManager"

    # Module to check and close if the program specified by the user
    # is installed and running. Relies on data from the ps aux.
    def close_running_application(self, close_command, base_handler):

        # First update the list of currently running programs
        self.update_list_of_running_programs(base_handler)

        # Final close system call command
        close_system_call_command = ''

        # Close command: Specifically not assigned any `type` to this
        # as it may be a list or a string depending on dynamic binding.
        close_command

        # Filter input command for common linguistic terms.
        close_command = self.filter_command(close_command)

        # Added `this` functionality. This enables an auto-detect on the Application
        # the user wants to close depending on the currently active window.
        if "this" in close_command:
            close_command = "this"

        # If `this` was specified by the user then updated command with the
        # active application's name.
        if "this" in close_command:
            close_system_call_command = base_handler.current_active_window.get_currently_active_appname()

        else:
            # Find the program that is referred here in the
            # list of running programs. If found prepare final command.
            for each_installed_app in base_handler.running_apps:
                for each_command in close_command:
                    if each_command.lower() in each_installed_app.lower():
                        # formulate the close command
                        close_system_call_command = each_installed_app.lower()
                        break

        # Null check if application is not found in running state. If running
        # use an apple-script to systematically close the running application.
        if close_system_call_command != '':
            base_handler.response_handler.respond_world("Closing "+close_system_call_command)
            close_system_call_command = 'osascript -e \'quit app \"'+close_system_call_command + '\"\''
            base_handler.exec_handler.exec_command(close_system_call_command)

        # Else either the application referred is not installed or it
        # is not running. Notify a negative response to the user.
        else:
            base_handler.response_handler.respond_world("Sorry sir, this application is not running")

    '''
    Helper module to update the apps currently running
    @param - base_handler (BaseMachine)
    '''
    def update_list_of_running_programs(self, base_handler):
        base_handler.running_apps, base_handler.running_apps_path = RunningApps().currectly_running_apps()

    '''
    Module to filter out general grammar words that could be used
    with close command. Sanitize the command and issue a fresh one.
    '''
    def filter_command(self, command):
        key = []
        command = command.split(" ")
        for command_token in command:
            matched = 0
            for filter_tokens in self.filterRef:
                if command_token == filter_tokens:
                    matched += 1
            if matched == 0:
                key.append(command_token)
        print "DEBUG: CloseManager: filter_command:"
        print key
        return key

'''
o = CloseManager()
o.update_list_of_running_programs(BaseMachine())
o.filter_command("close itunes")
'''