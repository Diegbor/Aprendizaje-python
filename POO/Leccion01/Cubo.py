#Definimos la clase
from time import altzone


class cubo:
    #Definimos los atributos
    def __init__(self,alto,largo,ancho):
        self.alto = alto
        self.largo = largo
        self.ancho = ancho
    #Definimos el metodo del volumen
    def volumen(self):
        return self.alto * self.largo * self.ancho

#Pedimos valores al usuario
alto = float(input("Introduzca el alto del prisma: "))
largo = float(input("Introduzca el largo del prisma: "))
ancho = float(input("Introduzca el ancho del prisma: "))

#Creamos el objeto cubo
cubo1 = cubo(alto,largo,ancho)
print(f"El volumen del cubo son: {cubo1.volumen()} metros cubicos")