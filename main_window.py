# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_remote_first = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_remote_first.setObjectName("listWidget_remote_first")
        self.gridLayout.addWidget(self.listWidget_remote_first, 0, 0, 1, 1)
        self.listWidget_remote_second = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_remote_second.setObjectName("listWidget_remote_second")
        self.gridLayout.addWidget(self.listWidget_remote_second, 0, 1, 1, 1)
        self.listWidget_local = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_local.setObjectName("listWidget_local")
        self.gridLayout.addWidget(self.listWidget_local, 0, 2, 1, 1)
        self.textEdit_terminal = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_terminal.setFont(font)
        self.textEdit_terminal.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_terminal.setObjectName("textEdit_terminal")
        self.gridLayout.addWidget(self.textEdit_terminal, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 642, 26))
        self.menubar.setObjectName("menubar")
        self.menuSession = QtWidgets.QMenu(self.menubar)
        self.menuSession.setObjectName("menuSession")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(MainWindow)
        self.actionConnect.setObjectName("actionConnect")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuSession.addAction(self.actionConnect)
        self.menuSession.addAction(self.actionQuit)
        self.menubar.addAction(self.menuSession.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SSH commander"))
        self.menuSession.setTitle(_translate("MainWindow", "Session"))
        self.actionConnect.setText(_translate("MainWindow", "Connect"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

