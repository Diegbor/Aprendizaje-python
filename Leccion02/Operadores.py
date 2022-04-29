#OPERADORES ARITMETICOS

#Suma
operandoA = 3
operandoB = 2
suma = operandoB + operandoA
print("Resultado de la suma: ", suma)
#Nueva forma de inprimir informacion
print(f"El resultado de la suma es: {suma}")

#Resta
resta = operandoA-operandoB
print(f"El resultado de la resta es: {resta}")

#Multiplicacion
multiplicacion = operandoA*operandoB
print(f"El resultado de la multiplicacion es: {multiplicacion}")

#Divicion
divicion = operandoA/operandoB
print(f"El resultado de la divicion es: {divicion}")

#Divicion Entera
diventera = operandoA//operandoB
print(f"El resultado de la divicion entera es: {diventera}")

#Modulo o reciduo 
modulo = operandoA % operandoB
print(f"El residuo de la divicion es: {modulo}")

#Exponente
exponente = operandoA ** operandoB
print(f"El resultado es: {exponente}")

#OPERADORES DE ASIGNACION

#Reasignacion 
operandoA += operandoB
print(operandoA)
operandoA -= operandoB
print(operandoA)
operandoA *= operandoB
print(operandoA)
operandoA /= operandoB
print(operandoA)
operandoA **= operandoB
print(operandoA)
operandoA //= operandoB
print(operandoA)
operandoA %= operandoB
print(operandoA)

#OPERADORES DE COMPARACION
a = 4
b = 2

#Comparacion
resultado = a == b
print(f"Resultado == {resultado}")

#Diferente de
resultado = a != b
print(f"Resultado != {resultado}")

#Mayor que
resultado = a > b
print(f"Resultado > {resultado}")

#Mayor o igual que
resultado = a >= b
print(f"Resultado >= {resultado}")

#Menor que 
resultado = a < b
print(f"Resultado < {resultado}")

#Menor o igual que 
resultado = a <= b
print(f"Resultado <= {resultado}")

#Ejercicio par o impar
numero = int(input("Ingresa un numero: "))
if numero % 2 == 0:
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

#Ejercicio Edad adulto
edadAdulto = 18
edadUsuario = int(input("Ingresa tu edad: "))
if edadUsuario >= edadAdulto:
    print(f"La persona con edad {edadUsuario} es mayor de edad")
else:
    print(f"La persona con edad {edadUsuario} es menor de edad")


#OPERADORES LOGICOS
#ejercicio operador and valor dentro de rango
ingreso = int(input("Ingresa un valor numerico: "))
if ingreso >= 0 and ingreso <= 5:
    print(f"El valor {ingreso} esta dentro de rango")
else: 
    print(f"El valor {ingreso} esta fuera de rango")

#Ejercicio operador or 
vacaciones = False
diaDescanso = True
if vacaciones or diaDescanso:
    print("Puede asistir al juego")
else: print("Tiene deberes por hacer")

#Ejercicio operador not
if not (vacaciones or diaDescanso):
    print("Tiene deberes por hacer")
else: 
    print("Puede asistir al juego")

#Ejercicio de rango de edad
nuevaEdad = int(input("Introduce tu edad: "))
if (nuevaEdad >= 20 and nuevaEdad<30) or (nuevaEdad >=30 and nuevaEdad<40):
    print("Estas dentro de los veintes o los treintas")
else:
    print("No estas dentro del rango de la juventud")

if (nuevaEdad >= 20 and nuevaEdad<30):
    print("Estas en los veintes")
elif (nuevaEdad >=30 and nuevaEdad<40):
    print("Estas en los treintas")
else:print("Estas fuera de la juventud")


#Ejercicio de tienda de libros
print("Proporciona los siguientes datos del libro: ")
nombre= input("Proporciona el nombre del libro: ")
id = int(input("proporciona el id del libro: "))
precio = float(input("Ingresa el precio del libro: "))
envio = input("Ingresa si el envio es gratis o no (True/False): ")

if envio == 'True':
    envio = True
elif envio == 'False':
    envio = False
else: 
    envio = "Valor incorrecto, debe escribir True o False"

#Para imprimir en varias lineas se usa la comilla triple
print(f'''
Nombre : {nombre}
ID : {id}
Precio : {precio}
Envio Gratuito : {envio} 
''')