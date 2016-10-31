# =====================================================================
# Manager to Initialize this application.
# All sub managers are initialized here. This includes Basemachine
# a.w.a. "Internal" managers that will be used to incorporate user
# actions with the help of this application.
# <+++++++++> Warning: This is a crucial integration module <+++++++++>
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

from BaseMachine import BaseMachine
from collections import defaultdict
from openManager import OpenManager
from closeManager import CloseManager
from questingManager import QuestingManager

class InitManger:

    # Initialize Base machine.
    base_handler = BaseMachine()

    # Initialize all 'external' Managers here.
    open_manager = OpenManager()
    close_manager = CloseManager()
    quest_manager = QuestingManager()

    # Standard commands that have a straight correlation with
    # the 'external' managers.
    # TODO: Make this JSON based.
    commands = {
        "open": {
            "open"
        },
        "close": {
            "close"
        },
        "quest": {
            "where",
            "what"
        }
    }  # this will define the states

    # A command issued by the user can fall within the below mentioned
    # categories. External managers are straightaway mapped to their
    # commands and the specific modules which are needed.
    # This dict is used for dynamic binding.
    states = {
        "open": open_manager.open_with_command,
        "close": close_manager.close_running_application
    }
    # If the user command doesn't fall in any of the above categories then,
    # this should be an error. Added a lambda (as default) mapped to internal
    # error manager.
    states = defaultdict(lambda: BaseMachine.error_handler.error_respond, states)

    '''
    Module to process the input tokens.
    Identify the type of command, return exit code.
    FYI: if the command is not found in the list of available commands
    then the default value is ILLEGAL initialized in base machine class.
    '''
    def process_tokens(self, rv):
        tokens = rv.split(' ')
        command_length = 1
        if len(tokens) > 0:
            for t in tokens:

                for c in self.commands:
                    if t in self.commands[c]:
                        # check if there are further command strings or not
                        if command_length == len(tokens):
                            # Then this is an error. Issue an underflow error code.
                            BaseMachine.exit_code = str(BaseMachine.ERR_COMM_UNDERFLOW) + "OOO" + str(
                                BaseMachine.ERR_COMM_UNDERFLOW)
                            return
                        else:
                            # Take the base command referred and the information referred by the user
                            # to process it later.
                            BaseMachine.exit_code = t + "OOO" + (" ".join(tokens[command_length:]))
                            return

                command_length += 1
        else:
            # Empty input, possibly time wait overflow in listen, hence 0 words
            self.base_handler.exit_code = str(self.base_handler.ERR_COMM_UNDERFLOW)+"OOO"+str(self.base_handler.ERR_COMM_UNDERFLOW)

        # TODO debug
        print(BaseMachine.exit_code)

    '''
    Based on the exit code from the process_tokens method
    we will switch to other states
    '''
    def start_machine(self):

        # Get the information from the exit code.
        next_state, residue_command = self.base_handler.exit_code.split('OOO')

        print "DEBUG: the next state is: "+next_state
        print "DEBUG: the residue command is: "+residue_command

        # Check if the residue is an error, handle response accordingly
        print "the type of next state is "+self.states[next_state].__module__
        if not self.states[next_state].__module__ == "ErrorManager":
            self.base_handler.response_handler.respond_world("executing command "+residue_command)
        self.states[next_state](residue_command, self.base_handler)

'''
o = InitManger()
o.process_tokens("can you tell me where pycharm")
print "DEBUG: (prog run - exit code is): "+o.base_handler.exit_code
o.start_machine()
'''

'''
r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
print("processing")
rv=r.recognize_google(audio)
print rv
os.system('Say -v Samantha -r 210 '+"Hello sir")
'''




