import requests
import JSONPARSER
import json
from JSONPARSER import Parser
from opencage.geocoder import OpenCageGeocode

class Delegater():
    def __init__(self):
        pass
        self.requested_services = ('yandex')
        self.api_key = None
        self.addr = None
        self.service = None
        self.json_response = None
        self.lang = None; self.long = None
        self.ParserJSON = JSONPARSER.Parser

    def analyze_input (self, service, addrQuery) :
        # self.api_key = api_input
        self.addr = addrQuery
        self.service = service

    def parse (self):
        
        if self.service == 'yandex':
            key = 'a96a2feb-3396-4d0d-a39b-3fb9b46e40b3'
            request = requests.get('https://geocode-maps.yandex.ru/1.x/?format=json&apikey={api}&geocode={addr}'.format(api=key, addr=self.addr))
            point_stuff = Parser.get_json_yandex(self,request.json())
            self.lang = point_stuff[0]
            self.long = point_stuff[1]
        elif self.service == 'opencage':
            key = 'd4f70793b57845e88558660fc597c7d2'
            geocoder = OpenCageGeocode(key)
            result = geocoder.geocode(self.addr)
            point_stuff = Parser.get_json_opencage(self, result)
            self.lang = str(point_stuff[1]);self.long = str(point_stuff[0])
        elif self.service == 'nominatim':
            response = self.fetch(self)
            tmp_stuff = Parser.get_json_nominatim(self, response)
            self.lang = tmp_stuff[0]; self.long = tmp_stuff[1]
        else:
            pass
            
    def get_point (self):
        stuff = [self.lang, self.long]
        return stuff


    def fetch(self):
        base_url = "https://nominatim.openstreetmap.org/search"
        params = {
            'q': self.addr,
            'format': 'geocodejson'
        }

        res = requests.get(url= base_url, params=params)

        if res.status_code == 200 :
            return res.json()
        else:
            return None
