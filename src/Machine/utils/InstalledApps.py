# =====================================================================
# Utility to get the installed Apps currently
# on the system
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

from SubprocessCall import SubprocessCall


class InstalledApps:

    def get_installed_apps(self):
        # create shell command to find all apps installed
        command = "find /Applications/ -name *.app 2>/dev/null"

        subprocess_call = SubprocessCall()

        # get the data in shell True mode
        app_data = subprocess_call.subprocess_call_getdata(command, True)
        index = 0
        while index < len(app_data):
            app_data[index] = app_data[index].split('\n')[0]
            index += 1

        print "Total number of apps: " + str(len(app_data))
        return app_data

'''
o = InstalledApps()
o.get_installed_apps()
'''