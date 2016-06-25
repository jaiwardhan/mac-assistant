# =====================================================================
# Manager to handle feedback to the user using voice controller
# available with Macs.
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

import os


class ResponseManager:

    def __init__(self):
        print "DEBUG_INIT: initialized response manager"

    # Module to handle outgoing voice responses.
    # Currently using samantha's voice and a 210 wpm rate of speech.
    # TODO: Voice and speech could be made configurable a.w.a. the rate
    def respond_world(self, response_for_user):
        os.system('Say -v Samantha -r 210 '+response_for_user)

