import csv
import sqlite3
import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication

from UI.mainUI import Ui_MainWindow
from new_window import NewWindow
from new_window2 import NewWindow2



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("data/coffee.db")
        self.show_elem()
        self.pushbutton.clicked.connect(self.open_new_window)
        self.pushbutton3.clicked.connect(self.update)
        self.pushbutton2.clicked.connect(self.open_new_window2)

    def show_elem(self):
        try:
            cur = self.con.cursor()
            self.result = cur.execute(f"""select * from types"""). \
                fetchall()
            self.result = [list(i) for i in self.result]
            # for i in self.result:
            #     i[3] = self.all_genre[str(i[3])]
            self.tableWidget.setColumnCount(7)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(self.result):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() +
                                             1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(i, j,
                                             QTableWidgetItem(str(elem)))
            self.tableWidget.setHorizontalHeaderLabels(
                ["id", "Название сорта", "Степень обжарки",
                 "Молотый/в зёрнах", "Описание вкуса", "Цена",
                 "Объём упаковки, гр"])
        except Exception as e:
            print(e)

    def open_new_window(self):
        try:
            self.window = NewWindow()
            self.window.show()
        except Exception as e:
            print(e)

    def open_new_window2(self):
        try:
            self.window = NewWindow2(self.lineEdit.text())
            self.window.show()
        except Exception as e:
            print(e)

    def update(self):
        with open('info.csv', encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            try:
                reader = list(reader)
                status = reader[0][0]
                if status == 'c':
                    id = reader[0][1]
                    name = reader[0][2]
                    level = reader[0][3]
                    type = reader[0][4]
                    about = reader[0][5]
                    cost = reader[0][6]
                    size = reader[0][7]
                    cur = self.con.cursor()
                    cur.execute(f"""update types set "Название сорта" = "{name}" 
                            WHERE id = {int(id)}""").fetchall()
                    cur.execute(f"""update types set "Степень обжарки" = "{level}" 
                                                WHERE id = {int(id)}""").fetchall()
                    cur.execute(
                        f"""update types set "Молотый/в зернах" = "{type}" 
                                                                    WHERE id = {int(id)}""").fetchall()
                    cur.execute(
                        f"""update types set "Описание вкуса" = "{about}" 
                                                                    WHERE id = {int(id)}""").fetchall()
                    cur.execute(
                        f"""update types set "Цена" = "{cost}" 
                                                                    WHERE id = {int(id)}""").fetchall()
                    cur.execute(
                        f"""update types set "Объем упаковки, гр" = "{size}" 
                                                                    WHERE id = {int(id)}""").fetchall()
                    self.show_elem()
                    self.con.commit()
                elif status == 'n':
                    print(self.result)
                    id = self.result[-1][0] + 1
                    name = reader[0][1]
                    level = reader[0][2]
                    type = reader[0][3]
                    about = reader[0][4]
                    cost = reader[0][5]
                    size = reader[0][6]
                    cur = self.con.cursor()
                    cur.execute(f"""INSERT INTO types(id, "Название сорта", "Степень обжарки", 
                            "Молотый/в зернах", "Описание вкуса", "Цена", "Объем упаковки, гр") VALUES({id},'{name}', '{level}',
    '{type}', '{about}', {cost}, {size})""").fetchall()
                    self.show_elem()
                    self.con.commit()
            except Exception as e:
                print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
