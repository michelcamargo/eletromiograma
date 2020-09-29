from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from client import Client
import numpy as np


class GUI:

    def __init__(self):

        # self.server1 = None
        self.client1 = Client()

        # GUI config
        self.app = QtGui.QApplication([])
        self.win = QtGui.QMainWindow()
        self.win.setObjectName("Analise graficos")
        self.win.resize(1000, 330)
        self.centralwidget = QtWidgets.QWidget(self.win)
        self.centralwidget.setObjectName("centralwidget")
        self.win.setCentralWidget(self.centralwidget)
        self.timer = QtCore.QTimer()
        # self.timer.timeout.connect(self.adquireDataGraph1)

        self.timer.timeout.connect(self.graphDataHandler)

        # layout auxs
        # gridLayout 1
        self.gridLayout1 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout1.setGeometry(QtCore.QRect(10, 140, 201, 173))

        # gridLayout 2
        self.gridLayout2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayout2.setGeometry(QtCore.QRect(10, 330, 201, 173))

        # labels
        # graph 1
        self.labelStatusGraph1 = QtWidgets.QLabel(self.gridLayout1)
        self.labelStatusGraph1.setObjectName("labelStatusGraph1")
        self.labelStatusGraph1.setText("Desconectado")
        self.label2Graph1 = QtWidgets.QLabel(self.gridLayout1)
        self.label2Graph1.setObjectName("label2Graph1")
        self.label2Graph1.setText("Status")
        self.labelPortaGraph1 = QtWidgets.QLabel(self.gridLayout1)
        self.labelPortaGraph1.setObjectName("labelPortaGraph1")
        self.labelPortaGraph1.setText("Porta:")
        self.labelGraph1 = QtWidgets.QLabel(self.gridLayout1)
        self.labelGraph1.setObjectName("labelGraph1")
        self.labelGraph1.setText("Ambiente: $" + self.client1.getHeader())
        self.labelIpGraph1 = QtWidgets.QLabel(self.gridLayout1)
        self.labelIpGraph1.setObjectName("labelIpGraph1")
        self.labelIpGraph1.setText("IP:")

        # Banner
        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(0, 0, 1041, 121))
        self.labelImage.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.labelImage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.labelImage.setTextFormat(QtCore.Qt.AutoText)
        self.labelImage.setPixmap(QtGui.QPixmap("./banner.jpg"))
        self.labelImage.setObjectName("labelImage")

        # buttons
        # graph 1
        self.btnIniciarGraph1 = QtWidgets.QPushButton(self.gridLayout1)
        self.btnIniciarGraph1.setObjectName("btnIniciarGraph1")
        self.btnIniciarGraph1.setText("Iniciar")
        self.btnIniciarGraph1.setEnabled(False)
        self.btnConectarGraph1 = QtWidgets.QPushButton(self.gridLayout1)
        self.btnConectarGraph1.setObjectName("btnConectarGraph1")
        self.btnConectarGraph1.setText("Conectar")
        self.btnSalvarGraph1 = QtWidgets.QPushButton(self.gridLayout1)
        self.btnSalvarGraph1.setObjectName("btnSalvarGraph1")
        self.btnSalvarGraph1.setText("Salvar")
        self.btnSalvarGraph1.setEnabled(False)
        self.btnDesconectarGraph1 = QtWidgets.QPushButton(self.gridLayout1)
        self.btnDesconectarGraph1.setObjectName("btnDesconectarGraph1")
        self.btnDesconectarGraph1.setText("Desconectar")
        self.btnDesconectarGraph1.setEnabled(False)
        self.btnPararGraph1 = QtWidgets.QPushButton(self.gridLayout1)
        self.btnPararGraph1.setObjectName("btnPararGraph1")
        self.btnPararGraph1.setText("Parar")
        self.btnPararGraph1.setEnabled(False)
        self.btnEncerrarGraph1 = QtWidgets.QPushButton(self.gridLayout1)
        self.btnEncerrarGraph1.setObjectName("btnEncerrarGraph1")
        self.btnEncerrarGraph1.setText("Encerrar")
        self.btnEncerrarGraph1.setEnabled(False)

        # inputs
        # graph 1
        self.inputIpGraph1 = QtWidgets.QLineEdit(self.gridLayout1)
        self.inputIpGraph1.setObjectName("inputIpGraph1")
        self.inputPortaGraph1 = QtWidgets.QLineEdit(self.gridLayout1)
        self.inputPortaGraph1.setObjectName("inputPortaGraph1")
        self.inputIpGraph1.setObjectName("inputIpGraph1")

        # controlBox1
        self.ControlGraphBox1 = QtWidgets.QGridLayout(self.gridLayout1)
        self.ControlGraphBox1.setContentsMargins(0, 0, 0, 0)
        self.ControlGraphBox1.setObjectName("ControlGraphBox1")

        self.ControlGraphBox1.addWidget(
            self.labelStatusGraph1, 1, 1, 0, 0, QtCore.Qt.AlignHCenter)

        self.ControlGraphBox1.addWidget(
            self.label2Graph1, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.ControlGraphBox1.addWidget(
            self.labelGraph1, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.ControlGraphBox1.addWidget(
            self.labelIpGraph1, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.ControlGraphBox1.addWidget(self.inputIpGraph1, 2, 1, 1, 1)
        self.ControlGraphBox1.addWidget(
            self.labelPortaGraph1, 3, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.ControlGraphBox1.addWidget(self.inputPortaGraph1, 3, 1, 1, 1)

        self.ControlGraphBox1.setColumnStretch(1, 1+1)

        self.ControlGraphBox1.addWidget(self.btnConectarGraph1, 4, 0, 1, 1)
        self.ControlGraphBox1.addWidget(self.btnDesconectarGraph1, 4, 1, 1, 1)
        self.ControlGraphBox1.addWidget(self.btnIniciarGraph1, 5, 0, 1, 1)
        self.ControlGraphBox1.addWidget(self.btnPararGraph1, 5, 1, 1, 1)
        self.ControlGraphBox1.addWidget(self.btnEncerrarGraph1, 6, 1, 1, 1)
        self.ControlGraphBox1.addWidget(self.btnSalvarGraph1, 6, 0, 1, 1)

        # graphView1
        self.graphicsView1 = PlotWidget(self.centralwidget)
        self.graphicsView1.setGeometry(QtCore.QRect(230, 140, 759, 171))
        self.graphicsView1.setObjectName("graphicsView1")
        #self.graphic1 = self.graphicsView1.plot(self.dataTempGraph1)

        # linhas de separacao
        # linha 1
        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setGeometry(QtCore.QRect(10, 120, 981, 20))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")

        # data Graph
        self.dataGraph1 = [0]
        self.dataTempGraph1 = np.zeros(10, dtype=int)

        # position
        self.position1 = 0

        self.graphic1 = self.graphicsView1.plot(self.dataTempGraph1)

        # buttons actions
        # Conectar
        self.btnConectarGraph1.clicked.connect(lambda: self.tryConnect())

        # Desconectar
        self.btnDesconectarGraph1.clicked.connect(
            lambda: self.tryDisconnect())

        # Iniciar
        self.btnIniciarGraph1.clicked.connect(lambda: self.iniciarGraph1())

        # parar
        self.btnPararGraph1.clicked.connect(lambda: self.paraGraph1())

        self.btnSalvarGraph1.clicked.connect(lambda: self.trySave())

        # Encerrar
        self.btnEncerrarGraph1.clicked.connect(lambda: self.encerrarGraph1())

    def tryConnect(self):
        # input_ip = str(self.inputIpGraph1.text())
        # input_port = int(self.inputPortaGraph1.text())
        # connected = self.client1.criarConexao(input_ip, input_port)

        # Meu Ip (Conectar direto):
        input_ip = str("10.0.0.105")
        input_port = int("2222")
        connected = self.client1.criarConexao(input_ip, input_port)

        if(connected):
            self.labelStatusGraph1.setText("Pronto")

            self.btnConectarGraph1.setEnabled(False)
            self.btnIniciarGraph1.setEnabled(True)
            self.btnDesconectarGraph1.setEnabled(True)
            self.inputIpGraph1.setReadOnly(True)
            self.inputPortaGraph1.setReadOnly(True)
        else:
            print("Nao conectado")

    def tryDisconnect(self):

        disconnected = self.client1.desconectar()

        if(disconnected):
            self.labelStatusGraph1.setText("Desconectado")
            self.btnConectarGraph1.setEnabled(True)
            self.btnDesconectarGraph1.setEnabled(False)
            self.btnIniciarGraph1.setEnabled(False)
            self.inputIpGraph1.setReadOnly(False)
            self.inputIpGraph1.setText("")
            self.inputPortaGraph1.setReadOnly(False)
            self.inputPortaGraph1.setText("")

    def iniciarGraph1(self):
        self.labelStatusGraph1.setText("Lendo dados...")
        self.btnDesconectarGraph1.setEnabled(False)
        self.btnIniciarGraph1.setEnabled(False)
        self.btnSalvarGraph1.setEnabled(False)
        self.btnEncerrarGraph1.setEnabled(False)
        self.btnPararGraph1.setEnabled(True)
        self.startPlotting()

    def paraGraph1(self):
        self.labelStatusGraph1.setText("Leitura parada...")
        self.btnPararGraph1.setEnabled(False)
        self.btnIniciarGraph1.setEnabled(True)
        self.btnSalvarGraph1.setEnabled(True)
        self.btnEncerrarGraph1.setEnabled(True)
        self.app.processEvents()
        self.stopPlotting()

    def encerrarGraph1(self):
        self.tryDisconnect()
        self.btnSalvarGraph1.setEnabled(False)
        self.btnEncerrarGraph1.setEnabled(False)
        self.dataGraph1 = [0]
        self.dataTempGraph1 = np.zeros(10)
        self.position1 = 0
        self.graphic1.setData(self.dataTempGraph1)
        self.graphic1.setPos(self.position1, 0)

    def updateGraph1(self):
        self.graphic1.setData(self.dataTempGraph1)
        self.graphic1.setPos(self.position1, 0)
        self.position1 += 1
        self.dataGraph1.append(self.dataTempGraph1[-1])
        self.graphic1.updateItems()
        self.graphicsView1.updateMatrix()

    def startPlotting(self):
        self.timer.start(1)

    def stopPlotting(self):
        self.timer.stop()

    def adquireDataGraph1(self, data):
        self.dataTempGraph1[:-1] = self.dataTempGraph1[1:]
        self.dataTempGraph1[-1] = data
        self.updateGraph1()

    def graphDataHandler(self):
        value = self.client1.reader()

        if(value):
            self.adquireDataGraph1(value)

    def trySave(self):
        fileName = self.client1.getHeader() + ".csv"

        self.labelStatusGraph1.setText("Salvando " + fileName)

        if(self.client1.writecsv(self.dataGraph1)):
            self.labelStatusGraph1.setText(fileName + " salvo.")

        else:
            self.labelStatusGraph1.setText(fileName + " não salvo.")


    def start(self):
        self.win.show()
        self.app.exec_()
