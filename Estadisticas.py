__author__ = 'cv.hernandez,vc.mendoza'

class Calculos:

    def Estadisticas (self,cadena):
        if cadena == "":
            return ([0])
        elif "," in cadena:
            numeros=cadena.split(',')
            print numeros
            for i in numeros:
                numeros2=tuple(numeros)
                print numeros2
            return([len(numeros2)])
        else:
            return([len(cadena)])
