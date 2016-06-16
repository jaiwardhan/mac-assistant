# @author: Jaiwardhan Swarnakar
import os


class ResponseManager:

    def __init__(self):
        print "DEBUG_INIT: initialized response manager"

    def respond_world(self, response_code):
        os.system('Say -v Samantha -r 210 '+response_code)

