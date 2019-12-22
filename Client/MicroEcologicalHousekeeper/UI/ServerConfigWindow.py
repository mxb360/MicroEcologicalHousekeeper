import sys

from MicroEcologicalHousekeeper.Core.ConfigData import AllConfigData

from ServerConfigUI import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets

class ServerConfigWindow:
    def __init__(self, parent=None):
        self.ui = Ui_Form()
        self.form = QtWidgets.QDialog(parent)
        self.ui.setupUi(self.form)
        self.form.setFixedSize(self.form.width(), self.form.height())  
        self.serverConfigData = AllConfigData().serverConfigData

        res, err = self.serverConfigData.getConfigDataAndCheck()
        if not res:
            print("获取配置文件失败！", err)
            host, port = '', ''
        else:
            host, port = self.serverConfigData.host, self.serverConfigData.port

        self.ui.serverHostLineEdit.setText(host)
        self.ui.serverPortLineEdit.setText(port)

        self.connect()

    def setServerConfig(self):
        self.serverConfigData.host = self.ui.serverHostLineEdit.text().strip()
        self.serverConfigData.port = self.ui.serverPortLineEdit.text().strip()

        res, e = self.serverConfigData.setConfigData()
        if not res:
            QtWidgets.QMessageBox.warning(self.form, "错误", "设置失败:" + str(e))
            return
        self.form.close()

    def exec(self):
        self.form.exec_()

    def show(self):
        self.exec()

    def connect(self):
        self.ui.okPushButton.clicked.connect(self.setServerConfig)
        self.ui.cancellPushButton.clicked.connect(self.form.close)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    serverConfigWindow = ServerConfigWindow()
    serverConfigWindow.show()
    sys.exit(app.exec_())
