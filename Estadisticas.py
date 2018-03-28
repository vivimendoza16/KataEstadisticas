__author__ = 'cv.hernandez,vc.mendoza'

class Calculos:

    def Estadisticas (self,cadena):
        if cadena == "":
            return ([0])
        else:
            print len(cadena)
            return([len(cadena)])
