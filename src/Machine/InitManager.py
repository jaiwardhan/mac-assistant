#!/usr/bin/env python3
from BaseMachine import BaseMachine
from collections import defaultdict
import speech_recognition as sr
import os


class InitManger(BaseMachine):
    def __init__(self):
        BaseMachine.__init__(self)

    commands = {"open"}  # this will define the states
    states = {
        "open": BaseMachine.open_manager.open_with_command

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
            BaseMachine.exit_code = str(BaseMachine.ERR_COMM_UNDERFLOW)+"OOO"+str(BaseMachine.ERR_COMM_UNDERFLOW)

        # TODO debug
        print(BaseMachine.exit_code)

    '''
    Based on the exit code from the process_tokens method
    we will switch to other states
    '''
    def start_machine(self):
        next_state, residue_command = BaseMachine.exit_code.split('OOO')
        print "DEBUG: the next state is: "+next_state
        # residue_command = BaseMachine.exit_code.split('OOO')[1]
        print "DEBUG: the residue command is: "+residue_command

        # check if the residue is an error, handle response accordingly
        if not self.states[next_state].__module__ == "ErrorManager":
            # normal response
            print "hello"
            BaseMachine.response_manager.respond_world("executing command "+residue_command)
        self.states[next_state](residue_command)

'''
o = InitManger()
o.process_tokens("open intellij in the background")
print "DEBUG: (prog run - exit code is): "+o.exit_code
o.start_machine()
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
#'''



