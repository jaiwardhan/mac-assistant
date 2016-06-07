
import os
class ResponseManager:
    def respond_world(self, response_code):
        os.system('Say -v Samantha -r 210 '+response_code)