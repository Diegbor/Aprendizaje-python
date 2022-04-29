numero = int(input("Proporciona un valor entre uno y tripas: "))
numeroTexto = ""
if numero == 1:
    numeroTexto = "Numero uno"
elif numero == 2:
    numeroTexto = "Numero dos"
elif numero == 3:
    numeroTexto = "Numero tres"
else:
    numeroTexto = "Valor fuera de rango"

print(f"Numero proporcionado: {numero} : {numeroTexto}")

#Condicion if else simplificada
condicion = True
print("Condicion verdadera") if condicion else print("Condicion falsa")

#Ejercicio estacion del año
mes = int(input("Ingresa el numero del mes que quieras (de 1 a 12): "))
estacion = None
if mes == 1 or mes == 2 or mes == 12:
    estacion = "Invierno"
elif mes == 3 or mes == 4 or mes ==5:
    estacion = "Primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "Verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "Otoño"
else: estacion = "Mes incorrecto"

print(f"Para el mes {mes} la estacion es {estacion}")

#Ejercicio estapas de la life 
edad = int(input("Ingresa tu edad: "))
mensaje = None
if edad >=0 and edad <10:
    mensaje = "La infancia es increible..."
elif edad >=10 and edad < 20:
    mensaje = "Muchos cambios y mucho estudio..."
elif edad >= 20 and edad <= 30:
    mensaje = "Amor y comienza el trabajo..."
else: mensaje = "Etapa de vida no reconocida"

print(f"Tu edad {edad}, {mensaje} ")