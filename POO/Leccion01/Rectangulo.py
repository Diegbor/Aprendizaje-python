#Definimos la clase
class rectangulo:
    #Definimos los atributos
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base 
    #Definimos el metodo
    def areaRectangulo(self):
        return self.base * self.altura

#Pedimos los datos de base y altura
base = float(input("Introduzca la base: "))
altura = float(input("Introduzca la altura: "))
#Creamos el objeto
rectangulo1 = rectangulo(base,altura)
print(f"El area del rectangulo 1 es: {rectangulo1.areaRectangulo()}")