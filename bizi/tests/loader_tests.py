# -.- encoding: utf-8 -.-

from unittest import TestCase
from unittest import skip
from bizi import loader
from bizi.models import Station
from hamcrest import *
from mock import Mock, MagicMock, ANY, patch
from bizi.loader import StationsLoader
import time 

# Implementar los tests y variar, usando asserts de unittest y hamcrest matchers

class StationsRawData2StationsTest(TestCase):

    def setUp(self):

        self.loader = StationsLoader()

        self.data = [
             {
                "coordenadas_p" : "41.649912000000000000,-0.863471000000000000",
                "y_coordinate" : 4613320.63448155,
                "tipocontenido_s" : "historico",
                "anclajesdisponibles_i" : 5,
                "text" : [
                   "C/ Doctor Iranzo -  C/ Escultor Benlliure",
                   "Datos de ocupación y localización de la estación bizi"
                ],
                "coordenadas_p_0_coordinate" : 41.649912,
                "category" : [
                   "Bizi"
                ],
                "id" : "bizi-101",
                "bicisdisponibles_i" : 15,
                "icon_t" : "http://www.zaragoza.es/contenidos/iconos/bizi/conbicis.png",
                "language" : "es",
                "estado_t" : "OPN",
                "last_modified" : "2013-03-08T07:33:00.63Z",
                "x_coordinate" : 678017.980345393,
                "description" : "Datos de ocupación y localización de la estación bizi",
                "uri" : "http://www.zaragoza.es/ciudad/viapublica/movilidad/bici/detalle_Bizi?oid=101",
                "texto_t" : "<ul><li>Estado: Operativa</li><li>Bicis disponibles: 15</li><li>Anclajes disponibles: 5</li></ul><p>Actualizado: 08:33</p>",
                "coordenadas_p_1_coordinate" : -0.863471,
                "title" : "C/ Doctor Iranzo -  C/ Escultor Benlliure"
             }
          ]

    def test_loader_raw_station_to_station(self):
        # Testear que un objeto estación raw (diccionario de atributos) se transforma a un objeto de tipo Station.
        #No testear explicitamente el tipo, sino comprobar propiedades. Evitar en el caso de strings comparar la cadena completa (usar matcher starts_with)
        raw_station = self.data[0]
        station = self.loader._raw_station_to_station(raw_station)


    def test_loader_raw_stations_to_stations_return_one_element_list(self):
        # Testear que raw_stations_to_stations devuelve una secuencia de un elemento. Usar tanto un matcher de hamcrest como un assertEquals de unittest
        stations = self.loader._raw_stations_to_stations(self.data)


class CachingStationsTest(TestCase):
    # Implementar todos los tests evitando llamar al servicio real, usando fakes de la función load_bizi_stations

    def setUp(self):
        self.loader = StationsLoader()

    def test_get_bizi_stations(self):
        # testear que la función get_bizi_stations devuelve estaciones si la función load_bizi_stations devuelve estaciones (mockear esta última
        # para que devuelva una lista de un objeto Station.
        # test simplemente para practicar con la función patch.object de mock
        res = self.loader.get_bizi_stations() 

    def test_get_bizi_stations_twice_only_calls_load_once_using_mock(self):
        # testear que si se llama dos veces seguidas a get_bizi_stations, solo se llama una vez a load_bizi_stations.
        # Hacerlo usando un objeto Mock. Usar como argumento de assert_called_once_with ANY.
        self.loader.get_bizi_stations(1) 
        self.loader.get_bizi_stations(1) 

    def test_get_bizi_stations_twice_only_calls_load_once_using_patch(self):
        # Mismo caso que el anterior, pero Hacerlo usando el context manager patch.object
        self.loader.get_bizi_stations() 
        self.loader.get_bizi_stations() 

    def test_get_bizi_stations_twice_only_calls_load_once_using_hamcrest_matcher_for_arg(self):
        # Mismo caso que el anterior, pero en lugar de usar ANY, utilizar para el argumento un matcher de hamcrest, gracias
        # a la función hamcrest.match_equality
        self.loader.get_bizi_stations(10) 
        self.loader.get_bizi_stations(10) 
        

    def test_get_bizi_stations_twice_in_5_mins_calls_load_twice(self):
        # testear que si se llama dos veces a get_bizi_stations, dejando entre llamadas más de n minutos (self.loader.refresh_time),
        # entonces, se llama dos veces a load_bizi_stations
        # debemos simular el paso del tiempo con patch sobre time.time
        self.loader.get_bizi_stations() 
        self.loader.get_bizi_stations() 

    def test_error_not_raised_on_connection_error(self):
        ## Supongamos que queremos que nuestro servicio no falle aun cuando la fuente de datos falle, siempre que tengamos datos recientes. 
        ## Testear que si la conexión con urllib2 falla, se devuelven datos igualmente. Recordar simular el paso del tiempo como en el anterior caso.
        self.loader.get_bizi_stations()
        self.loader.get_bizi_stations() 

