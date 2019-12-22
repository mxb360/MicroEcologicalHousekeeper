import sys

from MicroEcologicalHousekeeper.UI.ServerConfigWindow import ServerConfigWindow
from MicroEcologicalHousekeeper.UI.HardwareConfigWindow import HardwareConfigWindow

from ClientUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class ClientWindow:
    def __init__(self, parent=None):
        self.ui = Ui_MainWindow()
        self.mainWindow = QtWidgets.QMainWindow(parent)
        self.ui.setupUi(self.mainWindow)
        self.mainWindow.setFixedSize(self.mainWindow.width(), self.mainWindow.height())  

        self.connect()

    def show(self):
        self.mainWindow.show()

    def openServerConfigWindow(self):
        self.serverConfigWindow = ServerConfigWindow(self.mainWindow)
        self.serverConfigWindow.exec()

    def openHardwareConfigWindow(self):
        self.hardConfigWindow = HardwareConfigWindow(self.mainWindow)
        self.hardConfigWindow.exec()

    def connect(self):
        self.ui.serverConfigPushButton.clicked.connect(self.openServerConfigWindow)
        self.ui.hardwareConfigPushButton.clicked.connect(self.openHardwareConfigWindow)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    clientWindow = ClientWindow()
    clientWindow.show()
    sys.exit(app.exec_())
