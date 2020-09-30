import socket
from server import Server
import csv
import re


class Client:

    def __init__(self):
        self.header = "default"
        self.readyData = None

    def getHeader(self):
        return self.header

    def setHeader(self, headTitle):
        self.header = headTitle

    def setReadyData(self, dataGraph):
        self.readyData = dataGraph

    def getReadyData(self):
        return self.readyData

    def criarConexao(self, ip, port):

        self.server1 = Server()

        if(self.server1.connect(ip, port)):

            print("Connected and listening to", ip, ":", port)

            return True

        else:
            print("Connection failed")
            return False

    def desconectar(self):
        if(self.server1.close()):

            self.server1 = None
            return True

        else:
            return False

    def reader(self):
        try:
            self.server1.receiveMsg()

            if(self.server1.getData()):
                data = self.server1.getData()
                # print("msg:", data, type(data))

                plotable = self.dataControl(data)

                return plotable

        except:
            print("message problem.")

    # Retorna ao plotable o valor ou false
    def dataControl(self, msg):
        try:
            # Número inteiro
            if(int(msg)):
                dataLimit = [-1024, 1024]

                # Retorna o número plotável
                if(int(msg) >= dataLimit[0] and int(msg) <= dataLimit[1]):
                    return int(msg)

                else:
                    print("out of limits:", int(msg))

                    return False

        except:
            # Se o valor não for plotável
            self.msgHandler(msg)
            return False

    def msgHandler(self, msg):
        rTag = r"^\#"
        tag = "#"
        rWriteRef = r"^\$"
        writeRef = "$"

        # Comando (#)
        if(bool(re.match(rTag, msg))):
            msg = msg.replace(tag, "")

            validCmd = self.cmdHandler(msg)

            # if(not(validCmd)):
            # print("not a command.")

        # Referência de ambiente csv ($)
        elif(bool(re.match(rWriteRef, msg))):
            msg = msg.replace(writeRef, "")
            print("Ambiente: ", msg)
            self.setHeader(msg)

    # Interpretador de comandos
    def cmdHandler(self, cmd):

        # cmdList = {
        #     "test": self.testFn(),
        #     "start": self.startFn(),
        #     "save": self.writecsv(),
        # }

        if(cmd == "con"):
            self.server1.sendMessage("connected")

            return True

        elif(cmd == "save"):
            info = self.getHeader() + ".csv"

            if(self.writecsv()):
                info += " salvo."
                self.server1.sendMessage(info)

                return True

            else:
                info += " NAO salvo."
                self.server1.sendMessage(info)

        else:
            return False

    def writecsv(self):
        try:
            fileName = self.getHeader() + ".csv"

            # with open("data.csv", "a", newline='') as file:
            with open(fileName, "a", newline='') as file:
                dataGraph = self.getReadyData()
                # writer = csv.writer(file, delimiter=",")

                writer = csv.writer(file)

                for i in dataGraph:
                    # writer.writerow(str(i))
                    writer.writerow([i])

            return True

        except:
            print("ex writecsv")
            return False
