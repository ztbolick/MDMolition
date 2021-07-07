import os.path
import subprocess

class Addigy:
    def __init__(self):
        self.binary = None
        self.dir = None
        self.path = None
        self.elements = []

        check_addigy_exists(self)

def check_addigy_exists(self):
    if os.path.isfile("/Library/Addigy/auditor"):
        self.elements.append("auditor")
    if os.path.isfile("/Library/Addigy/collector"):
        self.elements.append("collector")
    if os.path.isfile("/Library/Addigy/go-agent"):
        self.elements.append("go-agent"
                             "")

def has_addigy_helper(self):
    if os.path.isdir("/Library/Application Support/JAMF/bin/jamfHelper.app"):
        return True
    else:
        return False

def check_addigy_path(self):
    checkShell = subprocess.run(['which', 'jamf'], capture_output=True, text=True).stdout

    if 'jamf' in checkShell:
        self.path = True
    else:
        self.path = False

def check_addigy_dir(self):
    if os.path.isdir("/Library/Addigy"):
        self.path = True
    else:
        self.path = False

def check_addigy_binary(self):
    pass