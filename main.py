import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QPropertyAnimation,QEasingCurve
from PyQt5 import uic
from PyQt5 import QtWidgets,QtWidgets
from PyQt5.uic import loadUi

from PyQt5 import QtCore
from PyQt5.QtCore import QPropertyAnimation
from PyQt5 import QtCore, QtGui, QtWidgets

import requests




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("example.ui",self)
        self.btn_Refrescar.clicked.connect(self.loadData)
        #BTN PAGE WIDGET
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_BD))
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Api))
        

    def loadData(self):
        url= 'https://62433a7fd126926d0c5d296b.mockapi.io/api/v1/usuarios'
        data=requests.get(url)
        row=0
        self.tableWidget.setRowCount(100)

        if data.status_code==200:
                
                data = data.json()
                for e in data:
                    
                    self.tableWidget.setItem(row,0, QtWidgets.QTableWidgetItem(e['id']))
                    self.tableWidget.setItem(row,1, QtWidgets.QTableWidgetItem(e['fec_alta']))
                    self.tableWidget.setItem(row,2, QtWidgets.QTableWidgetItem(e['user_name']))
                    self.tableWidget.setItem(row,3, QtWidgets.QTableWidgetItem(e['codigo_zip']))
                    self.tableWidget.setItem(row,4, QtWidgets.QTableWidgetItem(e['credit_card_num']))
                    self.tableWidget.setItem(row,5, QtWidgets.QTableWidgetItem(e['credit_card_ccv']))
                    self.tableWidget.setItem(row,6, QtWidgets.QTableWidgetItem(e['cuenta_numero']))
                    self.tableWidget.setItem(row,7, QtWidgets.QTableWidgetItem(e['direccion']))
                    self.tableWidget.setItem(row,8, QtWidgets.QTableWidgetItem(e['geo_latitud']))
                    self.tableWidget.setItem(row,9, QtWidgets.QTableWidgetItem(e['geo_longitud']))
                    self.tableWidget.setItem(row,10, QtWidgets.QTableWidgetItem(e['color_favorito']))
                    self.tableWidget.setItem(row,11, QtWidgets.QTableWidgetItem(e['ip']))
                    self.tableWidget.setItem(row,12, QtWidgets.QTableWidgetItem(e['auto']))
                    self.tableWidget.setItem(row,13, QtWidgets.QTableWidgetItem(e['auto_modelo']))
                    self.tableWidget.setItem(row,14, QtWidgets.QTableWidgetItem(e['auto_tipo']))
                    self.tableWidget.setItem(row,15, QtWidgets.QTableWidgetItem(e['auto_color']))
                    self.tableWidget.setItem(row,16, QtWidgets.QTableWidgetItem(e['fec_birthday']))
                    
                    row=row+1
       

    


# main
if __name__ == "__main__":
   
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())
