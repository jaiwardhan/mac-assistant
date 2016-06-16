from utils.RunningApps import RunningApps
import operator
from BaseMachine import BaseMachine
import subprocess


class CloseManager:

    # open filters and constants
    filterRef = ["up", "the", "in", "for", "me", "please", "copy", "instance", "a", "of"]

    def __init__(self):
        print "DEBUG_INIT: Initialized CloseManager"

    '''
    module to check if a program is running or not

    def if_this_program_is_runinng(self, program_name, base_handler):
        hash_map = {}

        # split the name of the program into possible parts which the user can give
        program_tokens = program_name.split(" ")

        # search by each token from the program name passed
        for program_token in program_tokens:
            # check it in all installed apps
            for each_installed_app in base_handler.apps_installed:
                # remove the redundant path and '.app' prefixes and suffixes
                # and split it coz installed app maybe multiple words long
                installed_app_prefix = each_installed_app.split('/')[-1].split(".app")[0].split(" ")
                for each_installed_app_prefix in installed_app_prefix:
                    # print "DEBUG---> each installed app is "+each_installed_app_prefix
                    if program_token.lower() in each_installed_app_prefix.lower():
                        print "the app is "+each_installed_app
                        # put this is hash map
                        p = subprocess.Popen(['pgrep', '-i', each_installed_app_prefix], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        process_id_list, err = p.communicate()
                        # out will be a list of PIDs with \n
                        print process_id_list
                        # split this by \n
                        process_id_list = process_id_list.split('\n')
                        for process_id in process_id_list:
                            if not process_id == '':
                                if each_installed_app_prefix not in hash_map.keys():
                                    hash_map[each_installed_app_prefix] = 1
                                else:
                                    hash_map[each_installed_app_prefix] = hash_map[each_installed_app_prefix] + 1
        # sort this dictionary by the most occuring application on the top
        if len(hash_map) > 0:
            most_occured_app = sorted(hash_map.keys(), key=operator.itemgetter(1), reverse=True)[0]
            print "the found pids are"
            print most_occured_app
            return most_occured_app
        else:
            return None
     '''
    def close_running_application(self, close_command, base_handler):
        # running_app = self.if_this_program_is_runinng(program_name,base_handler)

        # Update the list of currently running programs
        self.update_list_of_running_programs(base_handler)

        # filter input command
        close_command = self.filter_command(close_command)

        # close system call command
        close_system_call_command = ''

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
        if not running_app is None:
            # found a running app with this name
            closing_command = "osascript -e \'quit app \""+running_app+"\"\'"
            # os.system('osascript -e \'quit app \"IntelliJ Idea\"\'')
            print closing_command
        '''

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