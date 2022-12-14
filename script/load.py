# for worker node
import os

def loadCheck():
    if int(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()) >= 20:
        return False