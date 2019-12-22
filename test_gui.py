# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_gui.ui'
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
from integr_rewrited import *
import numpy as np

class Opening_win(object):

    def pushing(self):#функция переключения на 2 окно
        self.window=QtWidgets.QMainWindow()
        self.second_win=Integr_win()
        self.second_win.setupUi(self.window)#setupUi creates a form from designer
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1073, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_but = QtWidgets.QPushButton(self.centralwidget)
        self.start_but.setGeometry(QtCore.QRect(360, 430, 301, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_but.setFont(font)
        self.start_but.setObjectName("start_but")

        self.start_but.clicked.connect(self.pushing)#переклбчение на окно 2

        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(70, 40, 931, 201))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 26))
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
        self.start_but.setText(_translate("MainWindow", "Розпочати роботу"))
        self.title_label.setText(_translate("MainWindow", "Обчислення інтеграла за формулою Сімпсона"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Opening_win()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
