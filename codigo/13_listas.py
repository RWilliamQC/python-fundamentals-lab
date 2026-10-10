# Definicion
lista1 = []
lista2 = [12, 12.3, "Trece", 12+6j, True, lista1]

# Tipo de dato
type(lista2)

# El acceso a sus elementos
# deseo acceder a sus elementos (o componentes) del inicio al final (izquierda a derecha) : 0 1 2 3 ...
# deseo acceder a sus elementos (o componentes) del final al inicio (derecha a izquierda) : -1 -2 -3 ...

# Segunda componente de la variable lista2
lista2[1]

# Antepenultima componente de la variable lista2
lista2[-3]

# Notacion SLICE
# tres primera componentes de lista2
lista2[:3]

# Ultimos dos elementos de lista2
lista2[-2:]

# Operaciones de concatenacion : +
# Operacion de repeticion : *

lista3 = lista2 + lista2[-3:]
lista4 = 2026*lista3
lista5 = 19 * lista3 + lista4 * 82

# Tipo de datos
lista6 = [lista1, lista2, lista3, lista4, lista5]
for lista in lista6:
    print(type(lista))

# Generemos una lista con elementos pseudoaleatorios
import random as rnd

# Iniciamos con una lista en blanco
datos = []

for i in range(15):
    # Utilizamos la operacion de concatenacion para actualizar los elementos de la variables datos
    datos = datos  + [rnd.randint(0,20)]

datos

# Funcion len : devuelve el numero de elementos
# Funciones : min, max, sum

# Numero de elementos de lista4
len(lista4)

# Suma de elementos de la variable datos
sum(datos)

# minimo
min(datos)

# maximo
max(datos)

sum(lista2)

# Obtencion de la lista de metodos que se puede aplicar a un dato de tipo lista : funcion dir
dir(lista6)

# Documentacion
help([].append)

# Valor actual de lista1
lista1

#
lista1.append(19)

# Nuevamente el metodo append
lista1.append("PIT705 : El peor curso de mi vida")
lista1

# Ejemplito
# Necesitamos generar un secuencia "aleatoria" de tamaño n con elementos enteros entre 1 y 6 (proveidos por el usuario)
# Implementemos un algoritmo/estrategia que les n por teclado y construya la lista de observaciones usando
# exclusivamente el metodo append

# Input
n = int(input("Ingresa el tamaño de la muestra : "))
muestra = []

# Estructura repetitiva para que el usuario provea las entradas (1-6)
i = 0
while i<n:
    valor = int(input(f"Observacion {i+1} (1-6) : "))
    # Validar el ingreso
    if (valor <  1) or (valor >6):
        print("Valor fuera de rango. Reingrese")
        continue
    muestra.append(valor)
    i = i+1


# Mostremos los valores proveidos por el usuario
print("Muestra obtenido por el usuario : " , muestra)

# Documentacion
help(datos.clear)

# Valor actual de lista1
lista1

# Apliquemos el metodo clear
lista1.clear()

# Valor actual en lista1
lista1

# Si DESEO ELIMINAR LA VARIABLE : lista1
# Comando del
del lista1

lista1

# Documentacion
help(lista6.copy)

# Creacion de una copia de mi variables datos
datos1 = datos
print("Datos Originales ", datos)
print("Copia de Datos ", datos1)

# Modifiquemos el penultimo elemento de la copia
datos1[-2] = 0

print(datos1)

# Veamos los datos originales
print(datos)

# Esto expone la necesidad de un metodo copy
# La manera correcta de crear una copia "independiente" de una lista
# es utilizar el metodo copy
datos_copy = datos.copy()

# Podemos modificar datos en la copia
datos_copy[-1] = 666
datos_copy[3] = 23

print("Modificaciones : ", datos_copy)
print("Originales : ", datos )

# Documentacion
help(datos1.count)

# List Comprehension
lista7 = [rnd.randint(16,20) for i in range(200)]

# tipo de dato
type(lista7)

# Numero de elementos
len(lista7)

# Numero de veces que se repite el valor 19
lista7.count(19)

lista7.count(0)

# Documentacion
help([].extend)

# Documentacion
help(list().index)

# Documentacion
help([].insert)

# Documentacion
help([].pop)

# Documentacion
help([].remove)

# Documentacion
help([].reverse)

# Documentacion
help([].sort)

