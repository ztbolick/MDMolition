import os.path
import subprocess


class Jamf:
    def __init__(self):
        self.binary = None
        self.dir = None
        self.path = None
        self.helper = None

        has_jamf_helper(self)
        check_jamf_path(self)
        check_jamf_dir(self)
        check_jamf_binary(self)

def has_jamf_helper(self):
    if os.path.isdir("/Library/Application Support/JAMF/bin/jamfHelper.app"):
        return True
    else:
        return False

def check_jamf_path(self):
    checkShell = subprocess.run(['which', 'jamf'], capture_output=True, text=True).stdout

    if 'jamf' in checkShell:
        self.path = True
    else:
        self.path = False


def check_jamf_dir(self):
    if os.path.isdir(""):
        print("Jamf detected in path")
        return True


def check_jamf_binary(self):
    j = False

    if os.path.isfile("/usr/local/jamf"):
        j = True
        print("Jamf detected in local")
    if os.path.isfile("/usr/local/jamf/bin/jamf"):
        j = True
        print("Jamf detected in path")

    if j:
        self.binary = True
    else:
        self.binary = False