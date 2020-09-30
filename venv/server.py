import socket


class Server:
    def __init__(self):
        self.data = None
        self.sock = None
        self.onlineIp = None
        self.onlinePort = None
        self.target = None

    def getData(self):
        return self.data

    def setData(self, msg):
        self.data = msg

    def getOnlineIp(self):
        return self.onlineIp

    def setOnlineIp(self, ip):
        self.onlineIp = ip

    def getOnlinePort(self):
        return self.onlinePort

    def setOnlinePort(self, port):
        self.onlinePort = port

    def setTarget(self, addr):
        self.target = addr

    def getTarget(self):
        return self.target

    def close(self):
        try:
            self.sock.close()
            return True
        except:
            return False

    def connect(self, ip, porta):
        try:
            # SOCK_DGRAM == UDP CONNECTION
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
            self.sock.setblocking(False)
            self.sock.bind((ip, porta))

            self.setOnlineIp = ip
            self.setOnlinePort = porta

            return True

        except:
            self.setOnlineIp = None
            self.setOnlinePort = None

            return False

    def receiveMsg(self):
        try:
            msg, addr = self.sock.recvfrom(128)
            msg = msg.decode("utf-8")

            self.setTarget(addr)

            if(msg != None):
                # print("accomplished:", msg)
                self.setData(msg)
                return True

        except:
            self.setData(False)

    def sendMessage(self, msg):
        try:
            # print("sending \"", msg, "\"to:", self.getTarget())
            ret = self.sock.sendto(msg.encode('utf-8'), self.getTarget())

        except:
            print("not sent.")
