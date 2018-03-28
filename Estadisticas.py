__author__ = 'cv.hernandez,vc.mendoza'

class Calculos:

    def Estadisticas (self,cadena):
        if cadena == "":
            return ([0,0])
        elif "," in cadena:
            numeros=cadena.split(',')
            numeros2=tuple(numeros)

            return([len(numeros2)])
        else:
            return([len(cadena),int(min(cadena))])
