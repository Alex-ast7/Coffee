import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushbutton = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton.setGeometry(QtCore.QRect(10, 40, 70, 30))
        self.pushbutton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton2.setGeometry(QtCore.QRect(90, 40, 70, 30))
        self.pushbutton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton3.setGeometry(QtCore.QRect(10, 660, 70, 30))
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 850, 570))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 40, 170, 30))
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(420, 40, 70, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 554, 28))
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
        self.pushbutton.setText(_translate("MainWindow", "Добавить"))
        self.pushbutton2.setText(_translate("MainWindow", "Изменить"))
        self.pushbutton3.setText(_translate("MainWindow", "Обновить"))
        self.label.setText(_translate("MainWindow", "Укажите id для взаимодействия"))

