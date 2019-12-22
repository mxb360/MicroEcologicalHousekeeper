import sys

from MicroEcologicalHousekeeper.Core.ConfigData import AllConfigData
from MicroEcologicalHousekeeper import Config
from MicroEcologicalHousekeeper.UI.HardwareConfigUI import Ui_Form

from PyQt5 import QtCore, QtGui, QtWidgets

class HardwareConfigWindow:
    def __init__(self, parent=None):
        self.ui = Ui_Form()
        self.form = QtWidgets.QDialog(parent)
        self.ui.setupUi(self.form)
        self.form.setFixedSize(self.form.width(), self.form.height())  
    
        self.deviceNameConfigData = AllConfigData.deviceNameConfigData
        self.deviceNameInit()

        self.ledHardwareConfigData = AllConfigData.ledHardwareConfigData
        self.ledHardwareInit()

        self.connect()
       

    def deviceNameInit(self):
        res, err = self.deviceNameConfigData.getConfigDataAndCheck()
        if not res:
            print("警告：获取deviceNameConfig配置失败：", err)
            name = ''
        else:
            name = self.deviceNameConfigData.name

        self.ui.deviceNameLineEdit.setText(name)

    def ledHardwareInit(self):
        res, err = self.ledHardwareConfigData.getConfigDataAndCheck()
        if not res:
            print('警告：LED获取配置出现错误：', err)
        
    def exec(self):
        self.form.exec_()

    def show(self):
        self.exec()

    def connect(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    hardwareConfigWindow = HardwareConfigWindow()
    hardwareConfigWindow.show()
    sys.exit(app.exec_())
