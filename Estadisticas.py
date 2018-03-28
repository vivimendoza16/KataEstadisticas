__author__ = 'cv.hernandez,vc.mendoza'

class Calculos:

    def Estadisticas (self,cadena):
        if cadena == "":
            return ([0])
        elif "," in cadena:
            return([len((int(cadena[0]), int(cadena[2])))])
        else:
            return([len(cadena)])
