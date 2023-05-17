"""
Simple test
"""

""" Importar la test class """
from django.test import SimpleTestCase

""" Importar el objeto del test """
from app import calculator as c


""" Se define la Test Class y la basamos en un caso de prueba simple """
class CalculatorTest(SimpleTestCase):
    
    """ Agregamos el test method """
    def test_sum_numeros(self):
        a = 5
        b = 7
        result = c.sun(a, b)
        
        self.assertEqual(result, 12)
        
    """ Para este caso se creo primero la prueba y posteriormente la funcion """
    def test_rest_numeros(self):
        a = 5
        b = 10
        result = c.rest(a, b)
        
        self.assertEqual(result, 5)