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
import cryptocode

import sqlite3




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("design.ui",self)
        self.btn_Refrescar.clicked.connect(self.loadData)
        self.btn_cargueMasivo.clicked.connect(self.loadBD)

        #BTN PAGE WIDGET
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_BD))
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_Api))
        

    def loadData(self):
        #LLave encriptada
        Encrypt_url= 'MPCeQL7hmvXEUEAnhOk9KxLzvsVhJwrZvvLkegc7jlAig0OQ5CzlaUjkau+oLbCfdsIH4svC3IZezZ4=*0ymOR3hsZ1X/6RaKNYNwTg==*ddI5HBK35SpCyGDo6TWnDA==*l50KGxzXJvaOB6suWGRhHQ=='
        data=requests.get(cryptocode.decrypt(Encrypt_url, "qwerty"))

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

    def loadBD(self):
         #LLave encriptada
        Encrypt_url= 'MPCeQL7hmvXEUEAnhOk9KxLzvsVhJwrZvvLkegc7jlAig0OQ5CzlaUjkau+oLbCfdsIH4svC3IZezZ4=*0ymOR3hsZ1X/6RaKNYNwTg==*ddI5HBK35SpCyGDo6TWnDA==*l50KGxzXJvaOB6suWGRhHQ=='
        data=requests.get(cryptocode.decrypt(Encrypt_url, "qwerty"))

        # Crea un objeto de conexión a la base de datos SQLite
        con = sqlite3.connect("Base_datos.db")

        row=0
        self.tableWidget_2.setRowCount(100)

        if data.status_code==200:
                
                data = data.json()



                for e in data:
                    
                    con.execute("insert into Tabla_Usuarios(id,fec_alta,user_name,codigo_zip,credit_card_num,credit_card_ccv,cuenta_numero,direccion,geo_latitud,geo_longitud,color_favorito,ip,auto,auto_modelo,auto_tipo,auto_color,fec_birthday) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (e['id'],e['fec_alta'],e['user_name'],e['codigo_zip'],e['credit_card_num'],e['credit_card_ccv'],e['cuenta_numero'],e['direccion'],e['geo_latitud'],e['geo_longitud'],e['color_favorito'],e['ip'],e['auto'],e['auto_modelo'],e['auto_tipo'],e['auto_color'],e['fec_birthday']))
                    
                    self.tableWidget_2.setItem(row,0, QtWidgets.QTableWidgetItem(e['id']))
                    self.tableWidget_2.setItem(row,1, QtWidgets.QTableWidgetItem(e['fec_alta']))
                    self.tableWidget_2.setItem(row,2, QtWidgets.QTableWidgetItem(e['user_name']))
                    self.tableWidget_2.setItem(row,3, QtWidgets.QTableWidgetItem(e['codigo_zip']))
                    self.tableWidget_2.setItem(row,4, QtWidgets.QTableWidgetItem(e['credit_card_num']))
                    self.tableWidget_2.setItem(row,5, QtWidgets.QTableWidgetItem(e['credit_card_ccv']))
                    self.tableWidget_2.setItem(row,6, QtWidgets.QTableWidgetItem(e['cuenta_numero']))
                    self.tableWidget_2.setItem(row,7, QtWidgets.QTableWidgetItem(e['direccion']))
                    self.tableWidget_2.setItem(row,8, QtWidgets.QTableWidgetItem(e['geo_latitud']))
                    self.tableWidget_2.setItem(row,9, QtWidgets.QTableWidgetItem(e['geo_longitud']))
                    self.tableWidget_2.setItem(row,10, QtWidgets.QTableWidgetItem(e['color_favorito']))
                    self.tableWidget_2.setItem(row,11, QtWidgets.QTableWidgetItem(e['ip']))
                    self.tableWidget_2.setItem(row,12, QtWidgets.QTableWidgetItem(e['auto']))
                    self.tableWidget_2.setItem(row,13, QtWidgets.QTableWidgetItem(e['auto_modelo']))
                    self.tableWidget_2.setItem(row,14, QtWidgets.QTableWidgetItem(e['auto_tipo']))
                    self.tableWidget_2.setItem(row,15, QtWidgets.QTableWidgetItem(e['auto_color']))
                    self.tableWidget_2.setItem(row,16, QtWidgets.QTableWidgetItem(e['fec_birthday']))
                    con.commit()
                    
                    row=row+1 

    


# main
if __name__ == "__main__":
   
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())
