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
        MainWindow.resize(929, 678)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setToolTip("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.listView_remote_second = QtWidgets.QListView(self.centralwidget)
        self.listView_remote_second.setObjectName("listView_remote_second")
        self.gridLayout.addWidget(self.listView_remote_second, 1, 1, 1, 1)
        self.listView_remote_first = QtWidgets.QListView(self.centralwidget)
        self.listView_remote_first.setObjectName("listView_remote_first")
        self.gridLayout.addWidget(self.listView_remote_first, 1, 0, 1, 1)
        self.listView_local = QtWidgets.QListView(self.centralwidget)
        self.listView_local.setObjectName("listView_local")
        self.gridLayout.addWidget(self.listView_local, 1, 2, 1, 1)
        self.textEdit_terminal = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_terminal.setFont(font)
        self.textEdit_terminal.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.textEdit_terminal.setObjectName("textEdit_terminal")
        self.gridLayout.addWidget(self.textEdit_terminal, 2, 0, 1, 3)
        self.lineEdit_remote_first_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_remote_first_path.setObjectName("lineEdit_remote_first_path")
        self.gridLayout.addWidget(self.lineEdit_remote_first_path, 0, 0, 1, 1)
        self.lineEdit_remote_second_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_remote_second_path.setObjectName("lineEdit_remote_second_path")
        self.gridLayout.addWidget(self.lineEdit_remote_second_path, 0, 1, 1, 1)
        self.lineEdit_local_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_local_path.setObjectName("lineEdit_local_path")
        self.gridLayout.addWidget(self.lineEdit_local_path, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 26))
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

