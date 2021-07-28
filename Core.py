import sys
from PyQt5.QtCore import QUrl
import requests
from requests.models import parse_header_links
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from requests import api
from folium import Map, Marker
import io
import JSONPARSER
import dbmodule.DBCONNECTION
import datetime
import mapper
import request_delegater

class Interface(QtWidgets.QMainWindow,mapper.Ui_mapper):
    
    def __init__(self) :
        super().__init__()
        self.services = ('nominatim', 'yandex', 'opencage')
        self.setupUi(self)
        self.cmbServices.addItems(self.services)
        self.btnAction.clicked.connect(self.parse)
        self.btnSave.clicked.connect(self.save)
        self.btnMap.clicked.connect(self.init_map)
        self.parser_json = JSONPARSER.Parser
        self.json_resp = None
        self.service = None
        self.logTime = str(datetime.datetime.now())
        self.input_query = None
        self.response = None
        self.description = None
        self.delegater = request_delegater.Delegater

    def parse(self):
        self.txtLongitude.clear(); self.txtLatitude.clear()
        self.query = self.txtQuery.toPlainText()
        self.delegater.analyze_input(self.delegater, self.services[self.cmbServices.currentIndex()], self.query)
        self.delegater.parse(self.delegater)
        self.txtLongitude.append(self.delegater.get_point(self.delegater)[0]); self.txtLatitude.append(self.delegater.get_point(self.delegater)[1])

    def save(self):
        self.response = str(self.txtLongitude.toPlainText() +' '+ self.txtLatitude.toPlainText())
        self.description = self.textEdit.toPlainText()
        values = (f"{self.service}",f"{self.logTime}",f"{self.query}", f"{self.response}", f"{self.description}", f"{self.json_resp}")
        dbmodule.DBCONNECTION.external_request('insert',values)
        dbmodule.DBCONNECTION.external_request('show_all', None)

    def init_map (self):
        coordinates = [self.txtLatitude.toPlainText(), self.txtLongitude.toPlainText()]
        layout = QVBoxLayout()
        self.setLayout(layout)

        map = Map(tiles="cartodbpositron",location=coordinates, zoom_start=18)
        Marker(location=coordinates, popup=self.description).add_to(map)
        data = io.BytesIO()
        map.save('stuff.html')
        
        web_view = QWebEngineView()
        web_view.load(QUrl("E:/python_Projects/Ild-Mapper/stuff.html"))
        web_view.show()
        layout.addWidget(web_view)



def main ():
    app = QtWidgets.QApplication(sys.argv)
    window = Interface()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()