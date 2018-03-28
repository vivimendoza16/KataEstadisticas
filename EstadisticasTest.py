from unittest import TestCase

from Estadisticas import Calculos
__author__ = 'cv.hernandez,vc.mendoza'

class EstadisticasTest(TestCase):
    def test_Estadisticas(self):
        self.assertEqual(Calculos().Estadisticas(""),[0,0,0,0], "arreglo elementos,minimo,maximoy promedio vacio")

    def test_Estadisticas_unNumero(self):
        self.assertEqual(Calculos().Estadisticas("5"),[1,5,5,5], "arreglo elementos,minimo,maximo un elemento")

    def test_Estadisticas_dosNumeros(self):
        self.assertEqual(Calculos().Estadisticas("5,1"),[2,1,5,3], "arreglo elementos,minimo,maximo dos elementos")

    #def test_Estadisticas_Numneros(self):
      #  self.assertEqual(Calculos().Estadisticas("5,2,11,6,3"),[5,2,11], "arreglo elementos,minimo N elementos")

