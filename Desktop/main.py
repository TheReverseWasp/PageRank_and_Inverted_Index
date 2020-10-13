from helpers import *

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
from PyQt5.QtGui import *

from multiprocessing import Pool

app = QApplication(sys.argv)

class Interfaz(QMainWindow):
    def __init__(self):
        self.carta_trampa = 0
        super(Interfaz, self).__init__()
        loadUi("interface.ui", self)
        self.setWindowTitle("Buscador de palabras con PageRank")
        self.btnSearch.clicked.connect(self.on_btnSearch_clicked)
    @pyqtSlot()
    def on_btnSearch_clicked(self):
        self.carta_trampa += 1
        if self.carta_trampa % 2 == 1:
            return
        self.tableWidget.setRowCount(0)
        start = time.time()
        print(self.edtToSearch.toPlainText())
        full_rows = searchWord(self.edtToSearch.toPlainText())
        end = time.time()
        print("tiempo: " + str(end - start))
        #En caso de fallar se produce una alerta
        for i in range(len(full_rows)):
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i,0, QTableWidgetItem(full_rows[i][0]))
            self.tableWidget.setItem(i,1, QTableWidgetItem(str(full_rows[i][1])))
        app.processEvents()

Widget = Interfaz()
Widget.show()
sys.exit(app.exec_())
