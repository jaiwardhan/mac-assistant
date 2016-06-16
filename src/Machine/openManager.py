# @author: Jaiwardhan Swarnakar
class OpenManager:
    # open filters and constants
    filterRef = ["up", "the", "in", "for", "me", "please", "copy", "instance", "a", "of"]
    open_options = {
        "fresh": " --fresh",
        "new": " --new",
        "hide": " --hide",
        "hidden": " --hide",
        "background": " --background",
        "locate": "--reveal",
        "finder": " --reveal",
        "reveal": " --reveal"
    }

    def __init__(self):
        print "DEBUG_INIT: initalized open manager"

    '''
    module to filter out general grammar words
    with the open command and retain all the
    possible arguments to be given
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
        return key

    '''
    module to find a list of additional options
    given with the command - referred with open
    '''
    def get_open_program_and_options(self, command):
        options = []
        program = []

        for token in command:
            # if this token is in open options, add it to
            # options list, else add to program list
            if token in self.open_options.keys():
                options.append(token)
            else:
                program.append(token)
        return program, options

    '''
    Module to open a file/App with user command as a parameter
    - filters the user command to system useable format
    '''
    def open_with_command(self, command, base_handler):
        open_command = ""
        is_an_installed_app = False
        # filter the command for common phrases
        filtered_command = self.filter_command(command)
        print "DEBUG: (command filtered, found this): "
        print filtered_command

        program, options = self.get_open_program_and_options(filtered_command)

        '''
        now attach the program if found to the output command if the said program if available
        '''
        # TODO: We can optimize this search later
        for eachInstalledApp in base_handler.apps_installed:
            # print "here filtCom is " + filtered_command[0] + " and checking in " + eachInstalledApp.lower()
            if program[0].lower() in eachInstalledApp.lower():
                # prepare command
                open_command = "open '" + eachInstalledApp + "'"
                is_an_installed_app = True
                break

        '''
        attach options given by the user to the command
        '''
        if is_an_installed_app:
            print "DEBUG: OpenManager: this app installed"
            for option in options:
                open_command += self.open_options[option]
                # now send it to execution

            base_handler.exec_handler.exec_command(open_command)
        else:
            print "DEBUG: OpenManager: this app is not installed"
            base_handler.response_handler.respond_world("No such program is installed")
