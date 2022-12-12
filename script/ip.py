import subprocess
def getIp():
    IPAddr = str(subprocess.check_output(['hostname', '-I'])).split(' ')[0].replace("b'", "")
    return IPAddr

    