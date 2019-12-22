# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'closing_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui  import *
from integr_rewrited import *
from test_gui import *

# last=integr_rewrited.I
# print(last.simps)

class Closing(object):
    def btn_exit(self):
        self.close()

    def retry(self):
        self.pushing()


    def pushing(self):  # функция переключения на 1 окно
        self.window = QtWidgets.QMainWindow()
        self.first_win = Opening_win()
        self.first_win.setupUi(self.window)  # setupUi creates a form from designer
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.enter_data = QtWidgets.QLabel(self.centralwidget)
        self.enter_data.setGeometry(QtCore.QRect(30, 20, 611, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.enter_data.setFont(font)
        self.enter_data.setObjectName("enter_data")

        # self.label = QtWidgets.QLabel("Відповідь:tut",Closing)
        # self.label.setGeometry(QtCore.QRect(30, 20, 611, 101))
        # self.font = QtGui.QFont()
        # self.font.setPointSize(18)
        # self.label.setFont(self.font)
        # self.label.setText("Відповідь:tut")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 210, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 410, 381, 101))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.btn_exit)
        self.pushButton.clicked.connect(self.pushing)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.display_value()

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enter_data.setText(_translate("MainWindow", "Відповідь: "))
        self.pushButton.setText(_translate("MainWindow", "Розпочати заново"))
        self.pushButton_2.setText(_translate("MainWindow", "Завершити програму"))
    # def display_value(self):
    #     #Integr_win.simps(self)
    #     self.enter_data.setText(enter_data+"Hi")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Closing()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

