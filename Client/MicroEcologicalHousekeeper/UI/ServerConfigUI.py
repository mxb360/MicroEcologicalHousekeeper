# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerConfigUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(372, 263)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 81, 16))
        self.label_2.setObjectName("label_2")
        self.serverHostLineEdit = QtWidgets.QLineEdit(Form)
        self.serverHostLineEdit.setGeometry(QtCore.QRect(110, 80, 231, 31))
        self.serverHostLineEdit.setObjectName("serverHostLineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 81, 16))
        self.label_3.setObjectName("label_3")
        self.serverPortLineEdit = QtWidgets.QLineEdit(Form)
        self.serverPortLineEdit.setGeometry(QtCore.QRect(110, 130, 231, 31))
        self.serverPortLineEdit.setObjectName("serverPortLineEdit")
        self.okPushButton = QtWidgets.QPushButton(Form)
        self.okPushButton.setGeometry(QtCore.QRect(150, 210, 93, 28))
        self.okPushButton.setObjectName("okPushButton")
        self.cancellPushButton = QtWidgets.QPushButton(Form)
        self.cancellPushButton.setGeometry(QtCore.QRect(250, 210, 93, 28))
        self.cancellPushButton.setObjectName("cancellPushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "服务器配置"))
        self.label.setText(_translate("Form", "服务器配置"))
        self.label_2.setText(_translate("Form", "服务器主机"))
        self.label_3.setText(_translate("Form", "服务器端口"))
        self.okPushButton.setText(_translate("Form", "确定"))
        self.cancellPushButton.setText(_translate("Form", "取消"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
