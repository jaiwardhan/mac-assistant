# =====================================================================
# Interaction Module.
# This module is the place where it all begins!
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================


from Machine import InitManager
import speech_recognition
import os

class Jarvis:

    def start_jarvis(self):
        o = InitManager.InitManger()
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            os.system('Say -v Samantha -r 210 ' + "Hello sir, what can I, do for you?")
            print("Say something!")
            audio = recognizer.listen(source)
        print("processing\n")
        rv = recognizer.recognize_google(audio)
        print rv
        os.system('Say -v Samantha -r 210 ' + "Processing your request")
        o.process_tokens(rv)
        o.start_machine()

j = Jarvis()
j.start_jarvis()
