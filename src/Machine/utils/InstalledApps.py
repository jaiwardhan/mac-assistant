import subprocess
import shlex


class InstalledApps:
    def getInstalledApps(self):
        command = "find /Applications/ -name *.app 2>/dev/null"
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        text = p.stdout.read()
        retcode = p.wait()

        # debug
        # print "Debug: loaded list of installed apps"
        # print text;
        text = text.split('\n')
        print "Total number of apps: " + str(len(text))
        return text
