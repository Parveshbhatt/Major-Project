# for worker node
import os

def loadCheck():
    if int(float(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))) >= 15:
        return True

        