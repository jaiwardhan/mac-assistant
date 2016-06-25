# =====================================================================
# Utility to get the currently-active-application-on-the-window's name.
# Uses AppKits NSWorkspace module to get the application name.
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

from AppKit import NSWorkspace


class CurrentActiveAppWindow:

    def get_currently_active_appname(self):

        # Get the active window application name
        active_app_name = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']

        return active_app_name
