#Definir funcion
def primerFuncion(nombre,apellido):
    print("Saludos desde mi funcion")
    print(f"Nombre: {nombre}, Apellido: {apellido}")

#Mandar a llamar a la funcion
primerFuncion("Juanito","Bananas")
#Funcion suma
def suma(a=0,b=0):
    return a+b
resultado = suma(10,12)
print(resultado)
#Funcion con argumentos variables
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres("Juan","Karla","Maria","Lorenzo","Puñetas","Ernesto")
#Funcion de parametros variables que suma todos los valores ingresados
#Con 1 asterisco almacena los parametros como tupla
def sumarValores(*valores):
    resultado = 0
    for valor in valores:
        resultado += valor
    return resultado
print(sumarValores(1,2,3,4,5,6,7,8,9,10))
#Funcion que multiplica todos los parametros dentro
def multiplicar(*multiplos):
    x=1
    for multi in multiplos:
        x *= multi
    return x
print(multiplicar(1,2,3,4,5))
#Funcion que almacena los parametros como diccionario
#Se hace con dos asteriscos en los parametros
def listarTerminos(**terminos):
    for llave,valor in terminos.items():
        print(f"Llave: {llave}, valor: {valor}")

listarTerminos(IDE='ambiente de desarrollo', NOMBRE='Boris',edad=23, novia=True)
#Funcion que despliega nombres en forma de lista
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ["Boris","Diego","Op"]
desplegarNombres(nombres)
#Va a desplegar las letras de un solo nombre en forma de lista
desplegarNombres("Diego")
#Desplegar valores enteros
desplegarNombres((10,111,12,123,12,1,1))

#Funciones recurcivas 
def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero *factorial(numero-1)
resultado=factorial(5)
print(f"El factorial de 5 es: {resultado}")
#Funcion recursiva que imprime numeros descendentes
def numerosDescendentes(numeros):
    if numeros >= 1:
        print(numeros)
        numerosDescendentes(numeros-1)
numerosDescendentes(10)
#Funcion calcular un pago con impuestos incluidos
def calcularTotal(pagoSinImpuesto,impuesto):
    return pagoSinImpuesto + pagoSinImpuesto*(impuesto*0.01)

pagoSinImpuesto = float(input("Proporciona el pago sin el impuesto: "))
impuesto = float(input("Proporciona el impuesto: "))
pagoConImpuesto=calcularTotal(pagoSinImpuesto,impuesto)
print(f"El pago con impuesto es: {pagoConImpuesto}")
#Funcion de gracos celcius a farenhait
def gradosFahrenheit(grados):
    return grados*(9/5)+32
def gradosCelcius(grados):
    return (grados-32)*(5/9)

grados = float(input("Introduzca los grados que quiere que sean transformados: "))
fahrenheit = gradosFahrenheit(grados)
celcius = gradosCelcius(grados)
print(f"Los grados en celcius son: {celcius}")
print(f"Los grados en fahrenheit son: {fahrenheit}")