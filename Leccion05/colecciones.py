#Definir una lista 
nombres = ["juan","Karla","ricardo","Maria"]
#Imprimir nombres
print(nombres)
#Imprimir nombres por indices
print(nombres[0])
print(nombres[1])
#Imprimir con indices negativos del ultimo al primero 
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
print(nombres[-4])
#Imprimir un rango
#Imprime el valor del indice del primer numero hasta el valor de un indice 
# menor del segundo numero
#En este caso se imprime el indice 0 y el indice 1
print(nombres[0:2])
#Ir del inicio de la lista hasta el indice sin incluirlo 
print(nombres[:3])
#Desde el indice indicado hasta el final de la lista
print(nombres[2:])
#Cambios de valor
nombres[3] = "Ivonne"
print(nombres)
#Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista") 


#Preguntar el largo de una lista
print(len(nombres))
#Agregar un elemento a las listas
nombres.append("Lorenzo")
print(nombres)
#Insertar elemento en un indice en especifico
nombres.insert(1,"Octavio")
print(nombres)
#Remover un elemento por valor
nombres.remove("Octavio")
print(nombres)
#Eliminar el ultimo valor agregado
nombres.pop()
print(nombres)
#Eliminar elemento en un indice indicado
del nombres[0]
print(nombres)
#Limpiar lista 
nombres.clear
print(nombres)
#Eliminar la lista por completo 
del nombres
#Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
for i in range(10):
    if i%3 == 0:
        print(i)
else: print("Fin del ciclo for")

#TUPLAS EN PYTHON
#Definir tupla
frutas = ("naranja","platano","guayaba")
#Largo de una tupla
print(len(frutas))
print(frutas)
#Acceder a un elemento
print(frutas[0])
#Navegacion inversa
print(frutas[-1])
#Acceder a un rango de valores
print(frutas[0:3])
#Recorrer elementos en tupla
for fruta in frutas:
    print(fruta, end=" ")
#Las tuplas no se pueden modificar, son estaticas
#Convertir de tupla a lista 
frutasLista = list(frutas)
frutasLista[0]="Pera"
#Convertir de lista a tupla
frutas = tuple(frutasLista)
print("\n",frutas)
#eliminar tupla
del frutas

#Ejercicio tupla lista
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for elemento in tupla:
    if elemento <= 5:
        lista.append(elemento)

print(lista)

#COLECCION DE TIPO SET(sin orden y sin indices)
#Definir un set
planetas={"marte","jupiter","venus"}
print(planetas)
#Largo de un set
print(len(planetas))
#Revisar si un elemento esta dentro del set
print("marte" in planetas)
#agregar elementos al set
#no puede haber dos elementos iguales
planetas.add("Tierra")
print(planetas)
#Eliminar elemento
planetas.remove("Tierra")
print(planetas)
#Eliminar elemento sin arrojar error
planetas.discard("jupiter")
print(planetas)
#Limpiar set
planetas.clear()
print(planetas)
#Eliminar set
del planetas

#DICCIONARIOS
#Definir el diccionario
diccionario = {
    "ide":"Ambiente de desarrollo integrado",
    "oop": "Programacion orientada a objetos",
    "dbms":"Esto no se que significa jaja"
}
print(diccionario)
#Largo del diccionario
print(len(diccionario))
#Acceder a los elementos 
print(diccionario["ide"])
#Otra forma de recuperar elementos
print(diccionario.get("oop"))
#Modificar elementos 
diccionario["ide"]="ambiente de desarrollo integrado"
print(diccionario)
#Recorrer elementos del diccionario
#Acceder a las llaves
for termino in diccionario:
    print(termino)
#Acceder a la llave y valor
for termino, valor in diccionario.items():
    print(termino,valor)
#Acceder solo a las llaves otra vez
for termino in diccionario.keys():
    print(termino)
#Acceder solo al valor
for valor in diccionario.values():
    print(valor)

#Comprobar existencia de elemento en diccionario
print("ide" in diccionario)
#Agregar elemento al diccionario
diccionario["PK"]="Llave primaria"
print(diccionario)
#Remover un elemento
diccionario.pop("ide")
print(diccionario)
#Limpiar diccionario
diccionario.clear()
print(diccionario)
#Eliminar variable diccionario
del diccionario