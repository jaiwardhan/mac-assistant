# Utility to get the installed Apps currently
# on the system
# @author: Jaiwardhan Swarnakar

from SubprocessCall import SubprocessCall


class InstalledApps:

    def get_installed_apps(self):
        command = "find /Applications/ -name *.app 2>/dev/null"
        subprocess_call = SubprocessCall()

        # get the data in shell True mode
        text = subprocess_call.subprocess_call_getdata(command, True)
        index = 0
        while index < len(text):
            text[index] = text[index].split('\n')[0]
            index += 1

        print "Total number of apps: " + str(len(text))
        return text

'''
o = InstalledApps()
o.get_installed_apps()
'''