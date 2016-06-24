# Utility to get the currently active application
# on the window's name
# @author: Jaiwardhan Swarnakar
from AppKit import NSWorkspace


class CurrentActiveAppWindow:

    def get_currently_active_appname(self):
        activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
        return activeAppName
