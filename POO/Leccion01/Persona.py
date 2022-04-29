from cgi import print_arguments


class Persona:
    #Con el metodo __init__ agregamos atributos a nuestra clase y los inicializamos
    #Tambien se pueden introducir tuplas y diccionarios 
    # con argumentos variables en la clase
    def __init__(self,nombre,apellido,edad,*valores,**terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    #Aqui definimos los metodos de la clase
    #Un metodo es el comportamiento que va a tener nuestro objeto
    def mostarDetalle(self):
        print(f"Objeto persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}")

#Creamos un objeto de tipo persona
persona1 = Persona("Boris","Rosales",23,"hola","esto","es","la","tupla",d="esto es el diccionario",m="manzana",p="pera")
persona1.mostarDetalle()
#Otra forma de mandar a llamar un metodo
# Persona.mostarDetalle(persona1)
#Se puede agregar atributos externos a un objeto de forma infependiente
#Pero estos atributos no se comparten con los demas objetos
# persona1.telefono = "5544473659" 
# print(persona1.telefono) #el atributo telefono solo lo tiene el objeto persona1
#persona2 no cuenta con el

# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)
#Crear un segundo objeto persona
persona2 = Persona("Diego","Rebollar",24)
persona2.mostarDetalle()
# print(f"Objeto persona2: {persona2.nombre}, {persona2.apellido}, {persona2.edad}")
#Modificar atributos de un objeto
# persona1.nombre = "Morderas"
# persona1.apellido = "Simurdiera"
# persona1.edad = 40
# print(f"Objeto persona 1: {persona1.nombre}, {persona1.apellido}, {persona1.edad}")
