import csv
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from UI.addEditCoffeeForm import NewWindowUI


class NewWindow(QMainWindow, NewWindowUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushbutton.clicked.connect(self.save_info)

    def save_info(self):
        try:
            name = self.input1.text()
            level = self.input2.text()
            type = self.input3.text()
            about = self.input4.text()
            cost = int(self.input5.text())
            size = int(self.input6.text())
            if name and level and type and about and cost and size:
                with open('info.csv', encoding='utf-8', mode='w', newline='') \
                        as f:
                    writer = csv.writer(f, delimiter=';', quotechar='"',
                                        quoting=csv.QUOTE_MINIMAL)
                    writer.writerow(['n', name, level, type, about, cost, size])
                self.close()
            else:
                self.error_label.setText('Неправильно заполнена форма')
        except Exception as e:
            self.error_label.setText('Неправильно заполнена форма')