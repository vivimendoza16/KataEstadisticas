from unittest import TestCase

from Estadisticas import Calculos
__author__ = 'cv.hernandez,vc.mendoza'

class EstadisticasTest(TestCase):
    def test_Estadisticas(self):
        self.assertEqual(Calculos().Estadisticas(""),[0], "arreglo vacio")

    def test_Estadisticas_unNumero(self):
        self.assertEqual(Calculos().Estadisticas("5"),[1], "un elemento")

