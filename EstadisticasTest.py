from unittest import TestCase

from Estadisticas import Calculos
__author__ = 'cv.hernandez,vc.mendoza'

class EstadisticasTest(TestCase):
    def test_Estadisticas(self):
        self.assertEqual(Calculos().Estadisticas(""),[0,0], "arreglo elementos,minimo vacio")

    def test_Estadisticas_unNumero(self):
        self.assertEqual(Calculos().Estadisticas("5"),[1], "un elemento")

    def test_Estadisticas_dosNumeros(self):
        self.assertEqual(Calculos().Estadisticas("5,2"),[2], "dos elementos")

    def test_Estadisticas_Numneros(self):
        self.assertEqual(Calculos().Estadisticas("5,2,11,6,3"),[5], "N elementos")

