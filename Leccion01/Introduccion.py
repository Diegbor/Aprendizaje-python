# Variables
x = 10
y = 20
z = x + y
print(z)

# Localidades de memoria
# la funcion id nos dice en que localidad de memoria se encuentra almacenado nuestro dato
print(id(x))
print(id(y))
print(id(z))

# Tipos de datos
# Tipo entero
print(x)
print(type(x))
# Tipo flotante
w = 10.2222
print(w)
print(type(w))
# Tipo string
a = "Hola mundo"
print(a)
print(type(a))
# Tipo booleano
b = False
c = True
print(b, c)
print(type(b), type(c))

# Cadena (string)
# #concatenacion
miGrupoFavorito = "Chicos que lloran"
comentario = "La mejor banda"
print("Mi grupo favorito es: " + miGrupoFavorito)
# imprimir si concatenar, agrega un espacio en automatico despues de cada cadena
print("Mi grupo favorito es:", miGrupoFavorito, comentario)
n1 = "1"
n2 = "2"
# concatenacion
print("Concatenacion:", n1 + n2)
# suma de numeros
# La funcion int cambia el tipo de dato a un entero
print("Suma:", int(n1) + int(n2))

# Tipos booleanos (bool)
q = True
print(q)
q = 3 > 2
print(q)
if q:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")
# Funcion input para procesar la entrada del usuario
usuario = input("Escribe un mensaje: ")
print(usuario)

# Conversion de tipo de datos
numero1 = int(input("Escribe un numero: "))
numero2 = int(input("Escribe otro numero: "))
resultado = numero1 + numero2
print(resultado)

# Ejercicio califica tu dia
dia = input("Como estuvo tu dia (del 1 al 10): ")
print("Mi dia estuvo de: " + dia)
