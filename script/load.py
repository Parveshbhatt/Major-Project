# for worker node
import os

def loadCheck():
    print(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
    return False