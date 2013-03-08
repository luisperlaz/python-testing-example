import urllib2
from json import load
from bizi.models import Station
import time

class StationsLoader(object):

    def __init__(self):
        self.refresh_time = 5 * 60
        self.__data = []
        self.__last_update = 0

    def get_bizi_stations(self, rows=50):
        if not self.__data or self._needs_update():
            try:
                stations = self.load_bizi_stations(rows)
                self._cache_data(stations)
                self._updated()
            except:
                # TODO: if the last time the data was successfully retrieved was long time ago, then raise the exception
                pass
        return self.__data

    def load_bizi_stations(self, rows=50):
        res = self._get_data(rows)
        return self._raw_stations_to_stations(res)

    def _get_data(self, rows=50):
        urlt = 'http://www.zaragoza.es/buscador/select?q=category:Bizi&wt=json&rows={}'.format(rows)
        res = load(urllib2.urlopen(urlt))
        estaciones = res['response']['docs']
        return estaciones

    def _raw_stations_to_stations(self, raw_stations):
        return [self._raw_station_to_station(rst) for rst in raw_stations]

    def _raw_station_to_station(self, raw_station):
        return Station(id=raw_station['id'], 
                    address=raw_station['title'], 
                    slots_available=raw_station['anclajesdisponibles_i'], 
                    bikes_available=raw_station['bicisdisponibles_i'])


    def _needs_update(self):
        currsecs = time.time()
        delta = currsecs - self.__last_update
        return delta > self.refresh_time

    def _updated(self):
        self.__last_update = time.time()
    
    def _cache_data(self, stations):
        self.__data = stations
        Station.objects.all().delete()
        for station in stations:
            station.save()
