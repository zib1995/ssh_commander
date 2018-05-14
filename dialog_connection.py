# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_connection.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog_connection(object):
    def setupUi(self, Dialog_connection):
        Dialog_connection.setObjectName("Dialog_connection")
        Dialog_connection.resize(366, 137)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog_connection.sizePolicy().hasHeightForWidth())
        Dialog_connection.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Dialog_connection)
        self.gridLayout.setObjectName("gridLayout")
        self.label_host = QtWidgets.QLabel(Dialog_connection)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_host.setFont(font)
        self.label_host.setTextFormat(QtCore.Qt.AutoText)
        self.label_host.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_host.setObjectName("label_host")
        self.gridLayout.addWidget(self.label_host, 0, 0, 1, 1)
        self.lineEdit_host = QtWidgets.QLineEdit(Dialog_connection)
        self.lineEdit_host.setObjectName("lineEdit_host")
        self.gridLayout.addWidget(self.lineEdit_host, 0, 1, 1, 3)
        self.label_password = QtWidgets.QLabel(Dialog_connection)
        self.label_password.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_password.setObjectName("label_password")
        self.gridLayout.addWidget(self.label_password, 1, 0, 1, 1)
        self.lineEdit_password = QtWidgets.QLineEdit(Dialog_connection)
        self.lineEdit_password.setAutoFillBackground(False)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.gridLayout.addWidget(self.lineEdit_password, 1, 1, 1, 3)
        self.pushButton_connect = QtWidgets.QPushButton(Dialog_connection)
        self.pushButton_connect.setObjectName("pushButton_connect")
        self.gridLayout.addWidget(self.pushButton_connect, 2, 2, 1, 1)
        self.pushButton_cancel = QtWidgets.QPushButton(Dialog_connection)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.gridLayout.addWidget(self.pushButton_cancel, 2, 3, 1, 1)

        self.retranslateUi(Dialog_connection)
        QtCore.QMetaObject.connectSlotsByName(Dialog_connection)

    def retranslateUi(self, Dialog_connection):
        _translate = QtCore.QCoreApplication.translate
        Dialog_connection.setWindowTitle(_translate("Dialog_connection", "Connection"))
        self.label_host.setText(_translate("Dialog_connection", "Host"))
        self.label_password.setText(_translate("Dialog_connection", "Password"))
        self.pushButton_connect.setText(_translate("Dialog_connection", "Connect"))
        self.pushButton_cancel.setText(_translate("Dialog_connection", "Cancel"))

