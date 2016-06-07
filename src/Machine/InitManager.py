#!/usr/bin/env python3
from BaseMachine import BaseMachine
from collections import defaultdict
from openManager import OpenManager
from closeManager import CloseManager

class InitManger:
    base_handler = BaseMachine()
    open_manager = OpenManager()
    close_manager = CloseManager()

    commands = {"open"}  # this will define the states
    states = {
        "open": open_manager.open_with_command

    }
    states = defaultdict(lambda: BaseMachine.error_handler.error_respond, states)

    '''
    module to process the input tokens
    Identify the type of command, return exit code
    FYI: if the command is not found in the list of available commands
    then the default value is ILLEGAL initialized in base class
    '''
    def process_tokens(self, rv):
        tokens = rv.split(' ')
        i = 1
        if len(tokens) > 0:
            for t in tokens:
                if t in self.commands:
                    # check if there are further command strings or not
                    if i == len(tokens):
                        BaseMachine.exit_code = str(BaseMachine.ERR_COMM_UNDERFLOW)+"OOO"+str(BaseMachine.ERR_COMM_UNDERFLOW)
                        return
                    else:
                        BaseMachine.exit_code = t+"OOO"+(" ".join(tokens[i:]))
                        return
                i += 1
        else:
            # empty input, possibly time wait overflow in listen, hence 0 words
            self.base_handler.exit_code = str(self.base_handler.ERR_COMM_UNDERFLOW)+"OOO"+str(self.base_handler.ERR_COMM_UNDERFLOW)

        # TODO debug
        print(BaseMachine.exit_code)

    '''
    Based on the exit code from the process_tokens method
    we will switch to other states
    '''
    def start_machine(self):
        next_state, residue_command = self.base_handler.exit_code.split('OOO')
        print "DEBUG: the next state is: "+next_state
        # residue_command = BaseMachine.exit_code.split('OOO')[1]
        print "DEBUG: the residue command is: "+residue_command

        # check if the residue is an error, handle response accordingly
        print "the type of next state is "+self.states[next_state].__module__
        if not self.states[next_state].__module__ == "ErrorManager":
            # normal response
            print "hello"
            self.base_handler.response_handler.respond_world("executing command "+residue_command)
        self.states[next_state](residue_command, self.base_handler)

#'''
o = InitManger()
o.process_tokens("can you please open itunes in the finder")
print "DEBUG: (prog run - exit code is): "+o.base_handler.exit_code
o.start_machine()
#'''

'''
r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
print("processing\n")
rv=r.recognize_google(audio)
print rv
os.system('Say -v Samantha -r 210 '+"Hello sir")
'''




