#Definimos la clase
class Aritmetica:
    """
    Clase de aritmetica en donde vamos a hacer operaciones
    sumar, restar, multiplicar, dividir, etc.
    """
    #Definimos los atributos
    def __init__(self,operandoA,operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    #Definimos los metodos
    #Metodo de suma
    def sumar(self):
        return self.operandoA + self.operandoB
    #Metodo de resta
    def restar(self):
        return self.operandoA - self.operandoB
    #Metodo de multiplicar
    def multiplicar(self):
        return self.operandoA * self.operandoB
    #Metodo de dividir
    def dividir(self):
        return self.operandoA / self.operandoB
#Creando un objeto de la clase aritmetica
aritmetica1 = Aritmetica(4,3)
print(f"Sumar: {aritmetica1.sumar()}")
print(f"Restar: {aritmetica1.restar()}")
print(f"Multiplicar: {aritmetica1.multiplicar()}")
#Con :.2f indicamos cuandos digitos despues del punto decimal queremos mostrar
#en este caso dos
print(f"Dividir: {aritmetica1.dividir():.2f}")