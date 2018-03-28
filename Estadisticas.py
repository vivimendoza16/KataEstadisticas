__author__ = 'cv.hernandez,vc.mendoza'

class Calculos:

    def Estadisticas (self,cadena):
        if cadena == "":
            return ([0,0])
        elif "," in cadena:
            numeros=cadena.split(',')
            numeros0=[int(i) for i in numeros]
            cantidad=len(numeros0)
            minimo=min(numeros0)
            return([cantidad,minimo])
        else:
            return([len(cadena),int(min(cadena))])
