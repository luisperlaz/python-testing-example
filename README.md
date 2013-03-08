python-testing-example
======================

Aplicación de ejemplo para el taller de testing en python en Agile Aragon 

Se ha implementado una mini aplicación en Django que simplemente lista las estaciones de bizi que hay en Zaragoza.
Su único propósito es demostrar el uso de algunas herramientas para testing en python.

Requisitos
----------
Python 2.7
- Librerías adicionales sobre python  (los nombres de las librerías se citan tal cual se obtienen con pip desde pypi)
* django
* mock
* pyhamcrest
* nose
* django-nose
* Se recomienda instalarlos con pip (http://www.pip-installer.org/en/latest/), bien sobre la instalación de python, o sobre un virtualenv (http://www.virtualenv.org/en/latest/)). 

¿Qué hacer?
-----------

* Descargar el repositorio, en el cual hay dos ramas: master y notests

* master contiene la aplicación de ejemplo con los tests implementados
* notests contiene la misma aplicación, pero con los tests sin implementar para, a modo de ejercicio, intentar completarlos.


Ejecutar la aplicación
----------------------

    $ python manage.py runserver

Abrir en un browser http: http://localhost:8000/bizi/stations


Ejecutar los tests
------------------

    $ python manage.py test --settings=test_settings

ejecutar tests concretos:

    $ python manage.py test --settings=test_settings bizi/tests/loader_tests.py
    $ python manage.py test --settings=test_settings bizi/tests/loader_tests.py:CachingStationsTest
    $ python manage.py test --settings=test_settings bizi/tests/loader_tests.py:CachingStationsTest.test_get_bizi_stations

Referencias
-----------

Documentación para resolver los tests:

* Unittest: http://docs.python.org/2/library/unittest.html#unittest.TestCase
* Nose: https://nose.readthedocs.org/en/latest/usage.html
* Matchers de Hamcrest: https://pyhamcrest.readthedocs.org/en/V1.7/tutorial
* python Mock: http://www.voidspace.org.uk/python/mock/getting-started.html#getting-started-with-mock

Otros:
* Intro muy breve a unittest y nose: http://es.wikieducator.org/Usuario:Luis.perez/sistemaspyaytozgz/testing
