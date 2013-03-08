# -.- encoding: utf-8 -.-

from unittest import TestCase
from unittest import skip
from bizi.loader import StationsLoader
from bizi.models import Station
from hamcrest import *
from nose.tools import timed

# Implementar los tests con unittest y hamcrest matchers
# Poner límite de tiempo a la ejecución de estos tests, puesto que dependen del
# servicio externo. Ayuda: ver el decorador timed de nose.tools

class LoaderTest(TestCase):

    def setUp(self):
        self.loader = StationsLoader()

    @timed(3)
    def test_loader_get_data_returns_data(self):
        # testear que devuelve datos (cualquiera). 
        res = self.loader._get_data()
        self.assertIsNotNone(res)
        assert_that(res, is_(not_none()))

    @timed(3)
    def test_loader_get_data_return_specified_rows(self):
        #testear que devuelve una lista de objetos de tamaño especificado
        res = self.loader._get_data(10)
        assert_that(res, has_length(10))

    @timed(3)
    def test_loader_load_stations_return_specified_rows(self):
        #testear que devuelve una lista de estaciones de tamaño especificado
        res = self.loader.load_bizi_stations(10)
        assert_that(res, has_length(10))

    @timed(3)
    def test_loader_load_stations_return_stations(self):
        # testear que devuelve una lista de objetos de tipo Station. Testear que TODOS los objetos tienen una propiedad 'id'.
        # Después testear explicitamente que son de tipo Station
        res = self.loader.load_bizi_stations(1)
        assert_that(res, has_length(greater_than(0)))
        assert_that(res, only_contains(has_property('id')))
        assert_that(res, only_contains(instance_of(Station)))
        
