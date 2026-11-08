from django.test import TestCase

# Create your tests here.

import unittest
from .views import calcular_emisiones_carbono


class TestCalculoEmisiones(unittest.TestCase):

    def test_calculo_nominal(self):
        resultado = calcular_emisiones_carbono(100)
        self.assertEqual(resultado, 40)

    def test_factor_emision_personalizado(self):
        resultado = calcular_emisiones_carbono(100, 0.5)
        self.assertEqual(resultado, 50)

    def test_consumo_cero(self):
        resultado = calcular_emisiones_carbono(0)
        self.assertEqual(resultado, 0)

    def test_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-100)
