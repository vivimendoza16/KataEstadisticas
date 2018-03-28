__author__ = 'cv.hernandez,vc.mendoza'

class Calculos:

    def Estadisticas (self,cadena):
        if cadena == "":
            return ([0,0])
        elif "," in cadena:
            numeros1=len((int(cadena[0]),int(cadena[2])))
            numeros2=min(int(cadena[0]),int(cadena[2]))
            return([numeros1,numeros2])
        else:
            return([len(cadena),int(min(cadena))])
