from Machine import InitManager
import speech_recognition
import os
o = InitManager.InitManger()
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = recognizer.listen(source)
print("processing\n")
rv=recognizer.recognize_google(audio)
print rv
os.system('Say -v Samantha -r 210 '+"Hello sir")
o.process_tokens(rv)
o.start_machine()
