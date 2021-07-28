import json

class Parser() :
    def __init__(self):
        pass
    
    def get_json_yandex(self,jsonObject):
        data = jsonObject
        dict = data['response']['GeoObjectCollection']['featureMember']
        geo_position = dict[0]['GeoObject']['Point']['pos']
        return str(geo_position).split(' ')
        
    def get_json_opencage(self, jsonObject):
        data = jsonObject
        dict = data[0]['geometry']
        lat = dict['lat']; lon = dict['lng']
        return [lat, lon]

    def get_json_nominatim(self, jsonObject):
        data = [json.dumps(jsonObject['features'][0]['geometry']['coordinates'][0], indent=2),
                json.dumps(jsonObject['features'][0]['geometry']['coordinates'][1], indent=2)]
        return data

            

