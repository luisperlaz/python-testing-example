# -.- encoding: utf-8 -.-

from bizi.models import Station
from django.test.testcases import TestCase
from django.contrib.auth.models import User
from unittest import skip
from mock import patch


class StationsViewTest(TestCase):
    # realizar estos tests evitando que se haga ninguna llamada a bizi.loader.StationsLoader. 
    # el código de la vista de listado acaba llamando a la carga de datos. Queremos aislar los tests
    # de la vista de la fuente de datos. Para ello, parchear primero a nivel de función, y después
    # a nivel de clase.

    def setUp(self):
        user = User(username="me", is_staff=1, is_active=1, is_superuser=1)
        user.set_password('me')
        user.save()
        self.client.login(username=user.username, password='me')

    def test_empty_list_stations(self):
        # testear que una petición get a /bizi/stations/ produce una respuesta ok 200.
        # es necesario evitar que se haga ninguna llamada al cargador de estaciones real.
        pass

        
    def test_list_stations(self):
        # testear que una petición get a /bizi/stations/ produce una respuesta ok 200 y muestra alguna estación en el listado.
        # Para ello es necesario preparar estaciones que serán leidas. Las estaciones se meten en BD, y se intentan refrescar con cada llamada
        # al listado. Evitar el refresco de datos usando el cargador de estaciones. Simplemente crear en BD las estaciones que se van a mostrar.

        Station(id='bizi-1', address='C/ cualquiera 1').save()
        Station(id='bizi-2', address='C/ cualquiera 2').save()

        pass

