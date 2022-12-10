import socket
def getIp():
    IPAddr=socket.gethostbyname(socket.gethostname())
    return IPAddr
