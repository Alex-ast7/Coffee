import csv
import sqlite3
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication
from UI.addEditCoffeeForm import NewWindow2UI


class NewWindow2(QMainWindow, NewWindow2UI):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.id = id
        self.con = sqlite3.connect("data/coffee.db")
        cur = self.con.cursor()
        self.result = cur.execute(f"""select * from types where id = 
                {int(self.id)}""").fetchall()
        self.input1.setText(self.result[0][1])
        self.input2.setText(self.result[0][2])
        self.input3.setText(self.result[0][3])
        self.input4.setText(self.result[0][4])
        self.input5.setText(str(self.result[0][5]))
        self.input6.setText(str(self.result[0][6]))
        self.pushbutton.clicked.connect(self.save_info)

    def save_info(self):
        try:
            id = self.id
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
                    writer.writerow(['c', id, name, level, type, about, cost, size])
                self.close()
            else:
                self.error_label.setText('Неправильно заполнена форма')
        except Exception as e:
            self.error_label.setText('Неправильно заполнена форма')