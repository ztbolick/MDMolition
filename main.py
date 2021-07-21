from Jamf import Jamf
from Addigy import Addigy
import subprocess


if __name__ == '__main__':
    # print("Starting MdMolition")
    # jamf = Jamf()
    # addigy = Addigy()
    # print(addigy.elements)

    arg = "which jamf"
    arg = arg.split()

    checkShell = subprocess.run(arg, capture_output=True, text=True).stdout
    
    print(checkShell)