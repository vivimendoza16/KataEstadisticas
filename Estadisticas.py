__author__ = 'cv.hernandez,vc.mendoza'

class Calculos:

    def Estadisticas (self,cadena):
        if cadena == "":
            return ([0,0])
        elif "," in cadena:
            numeros=cadena.split(',')
            print numeros
            numeros0=[int(i) for i in numeros]
            print numeros0
            numeros1=len(numeros0)
            print numeros1
            numeros2=min(numeros0)
            print numeros2
            return([numeros1,numeros2])
        else:
            return([len(cadena),int(min(cadena))])
