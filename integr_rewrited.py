# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'win_integr_rewrited.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
import PyQt5
from PyQt5 import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui  import *
from closing_win import *
import numpy as np


class Integr_win(object):

    def pushing1(self):#функция переключения на 3 окно
        self.window=QtWidgets.QMainWindow()
        self.third_win=Closing()
        self.third_win.setupUi(self.window)#setupUi creates a form from designer
        self.window.show()

    def simps(self):
        a=self.input_a()
        b=self.input_b()
        N=self.input_N()
        y=self.input_y()
        dx = (b-a) / N  # step
        x = np.linspace(a, b, N + 1)
        f = eval(y)
        S = dx / 3 * np.sum(f[0:-1:2] + 4 * f[1::2] + f[2::2])  # sums all list's elements with changes
        print("Answer is ", S)
        return S

    # def pushing(self):#функция переключения на 3 окно
    #     self.window=QtWidgets.QMainWindow()
    #     self.second_win=Closing()
    #     self.second_win.setupUi(self.window)#setupUi creates a form from designer
    #     self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enter_data = QtWidgets.QLabel(self.centralwidget)
        self.enter_data.setGeometry(QtCore.QRect(10, 30, 611, 101))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.enter_data.setFont(font)
        self.enter_data.setObjectName("enter_data")
        self.enter_N = QtWidgets.QLabel(self.centralwidget)
        self.enter_N.setGeometry(QtCore.QRect(10, 450, 911, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.enter_N.setFont(font)
        self.enter_N.setObjectName("enter_N")


        self.mult = QtWidgets.QLabel(self.centralwidget)
        self.mult.setGeometry(QtCore.QRect(720, 180, 331, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mult.setFont(font)
        self.mult.setObjectName("mult")


        self.hint = QtWidgets.QLabel(self.centralwidget)
        self.hint.setGeometry(QtCore.QRect(710, 110, 341, 81))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro")
        font.setPointSize(18)
        font.setItalic(False)
        self.hint.setFont(font)
        self.hint.setObjectName("hint")


        self.enter_data_2 = QtWidgets.QLabel(self.centralwidget)
        self.enter_data_2.setGeometry(QtCore.QRect(450, 180, 101, 91))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.enter_data_2.setFont(font)
        self.enter_data_2.setObjectName("enter_data_2")


        self.line_func = QtWidgets.QLineEdit(self.centralwidget)
        self.line_func.setGeometry(QtCore.QRect(130, 210, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.line_func.setFont(font)
        self.line_func.setObjectName("line_func")


        self.line_N = QtWidgets.QLineEdit(self.centralwidget)
        self.line_N.setGeometry(QtCore.QRect(830, 460, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.line_N.setFont(font)
        self.line_N.setObjectName("line_N")


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(430, 580, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.simps)
        self.pushButton.clicked.connect(self.pushing1)

        self.enter_data_3 = QtWidgets.QLabel(self.centralwidget)
        self.enter_data_3.setGeometry(QtCore.QRect(10, 170, 101, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.enter_data_3.setFont(font)
        self.enter_data_3.setObjectName("enter_data_3")


        self.line_b = QtWidgets.QLineEdit(self.centralwidget)
        self.line_b.setGeometry(QtCore.QRect(60, 190, 51, 41))
        self.line_b.setObjectName("line_b")


        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 240, 51, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")


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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enter_data.setText(_translate("MainWindow", "Введіть дані(за параметром х):"))
        self.enter_N.setText(_translate("MainWindow", "Введіть к-сть проміжків для інтегрування N(парне число):"))
        self.mult.setText(_translate("MainWindow", "піднесення до степеня = \'**\'"))
        self.hint.setText(_translate("MainWindow", "Підказка для вводу даних:"))
        self.enter_data_2.setText(_translate("MainWindow", "dx "))
        self.pushButton.setText(_translate("MainWindow", "Інтегрувати"))
        self.enter_data_3.setText(_translate("MainWindow", "∫"))

    def input_b(self):
        textboxb=int(self.line_b.text())
        print(textboxb)
        return textboxb

    def input_a(self):
        textboxa=int(self.lineEdit_2.text())
        print(textboxa)
        return textboxa

    def input_N(self):
        textboxN=int(self.line_N.text())
        print(textboxN)
        return textboxN

    def input_y(self):
        textboxy=self.line_func.text()
        print(textboxy)
        return textboxy
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Integr_win()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



