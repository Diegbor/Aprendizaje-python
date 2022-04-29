#Ciclo while
contador = 0
while contador <=10:
    print(contador)
    contador += 1
else:
    print("fin del ciclo while")

contador = 5
while contador >=1:
    print(contador)
    contador -= 1
else:
    print("Fin del ciclo while")

#Ciclo for
cadena = "hola"
for letra in cadena:
    print(letra)
else: 
    print("Fin ciclo for")


for letra in "Holanda":
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        #break es para romper el ciclo, haciendo que ya no se ejecute lo que va despues del break 
        break
else:
    print("Fin ciclo for")

#Palabra continue
#rango es para asignar un rango de valores
for i in range(6):
    if i%2 == 0:
        print(f"Valor: {i}")

#continue
for i in range(6):
    if i%2 != 0:
        continue
    print(f"Valor: {i}")