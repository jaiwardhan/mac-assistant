# @author: Jaiwardhan Swarnakar
from utils.RunningApps import RunningApps

class CloseManager:

    # open filters and constants
    filterRef = ["up", "the", "in", "for", "me", "please", "copy", "instance", "a", "of", "alright", "window"]

    def __init__(self):
        print "DEBUG_INIT: Initialized CloseManager"

    def close_running_application(self, close_command, base_handler):
        # running_app = self.if_this_program_is_runinng(program_name,base_handler)

        # Update the list of currently running programs
        self.update_list_of_running_programs(base_handler)

        # close system call command
        close_system_call_command = ''
        close_command
        # filter input command
        close_command = self.filter_command(close_command)

        # add `this` functionality
        if "this" in close_command:
            close_command = "this"

        if "this" in close_command:
            close_system_call_command = base_handler.current_active_window.get_currently_active_appname()

        else:
            # find the program that is referred here in the
            # list of running programs
            for each_installed_app in base_handler.running_apps:
                for each_command in close_command:
                    if each_command.lower() in each_installed_app.lower():
                        # formulate the close command
                        close_system_call_command = each_installed_app.lower()
                        break

        if close_system_call_command != '':
            base_handler.response_handler.respond_world("Closing "+close_system_call_command)
            close_system_call_command = 'osascript -e \'quit app \"'+close_system_call_command + '\"\''
            base_handler.exec_handler.exec_command(close_system_call_command)

        else :
            base_handler.response_handler.respond_world("Sorry sir, this application is not running")

    '''
    Helper module to update the apps currently running
    @param - base_handler (BaseMachine)
    '''
    def update_list_of_running_programs(self, base_handler):
        base_handler.running_apps, base_handler.running_apps_path = RunningApps().currectly_running_apps()

    '''
    module to filter out general grammar words
    that could be used with close command
    '''
    def filter_command(self, command):
        key = []
        command = command.split(" ")
        for i in command:
            matched = 0
            for j in self.filterRef:
                if i == j:
                    matched += 1
            if matched == 0:
                key.append(i)
        print "DEBUG: CloseManager: filter_command:"
        print key
        return key

'''
o = CloseManager()
o.update_list_of_running_programs(BaseMachine())
o.filter_command("close itunes")
'''