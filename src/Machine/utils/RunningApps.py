# =====================================================================
# Utility to get the Apps currently running on the system.
# Systematically returns the Appname and the main executable path
# of the running application
# @author: Jaiwardhan Swarnakar, 2016
# =====================================================================

from SubprocessCall import SubprocessCall


class RunningApps:

    # Module to return the apps currently running on the system.
    # Returns a list of Apps and their paths.
    def currectly_running_apps(self):

        subprocess_call = SubprocessCall()

        # add a listener to stdout for the output of `ps aux` and process it
        # get the data in shell False mode
        data = subprocess_call.subprocess_call_getdata(['ps', 'aux'], False)

        # data variables
        running_app_path = ''
        running_app = ''
        running_apps = []
        running_apps_path = []

        # construct the path from the obtained tuple list
        for each_tuple in data:

            # break the tuple data, and join the split path to
            # reconstruct the application path
            each_tuple = each_tuple.split('/')[1:-1]

            # only choose valid application outputs and Applications by the user
            # We are doing this deliberately so that we don't mess up system apps
            if len(each_tuple) > 0 and each_tuple[0].lower() == "applications":
                for tuple_data in each_tuple:
                    running_app_path = running_app_path + "/" + tuple_data

                # remove redundant path extension inside the .app folder
                # to get the main running app name
                if len(running_app_path) > 0:
                    running_app = running_app_path.split('.app/Contents')[0].split('/')[-1]
                    running_app_path = running_app_path.split('.app/Contents')[0] + '.app'

                    # append in the list to be returned
                    running_apps_path.append(running_app_path)
                    running_apps.append(running_app)
            running_app_path = ''

        return running_apps, running_apps_path

'''
o = RunningApps()
app, path = o.currectly_running_apps()
i = 0
while i < len(app):
    print app[i] + '\n' + path[i] + '\n'
    i += 1
print i
'''