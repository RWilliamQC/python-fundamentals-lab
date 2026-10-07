# Ejemplito : Tabla de multiplicar
tabla = int(input("Ingrese el numero de la tabla : "))
for factor in range(1,11):
    resultado = tabla * factor
    print("%d x %d = %d" %(tabla, factor, resultado))

# Ejemplito : Conteo regresivo
for cta in range(10, 0 , -1):
    print(cta)
print("nave espacial : Despegue ")

# Acumulador
n = int(input("¿ Hasta que numero deseas sumar : ?"))

# Inicializamos antes del bucle un acumulador
acumulador = 0

# Estructura repetitiva
for numero in range(1, n+1):
    acumulador = acumulador + numero # actualizamos el valor de la variable acumulador dentro del bucle

# Resultados
print("Suma de 1 a %d es : %d " %(n, acumulador))

# Recorramos una variable de tipo cadena de caracter (str) elemento a elemento
frase = input("Ingresa una frase o palabra : ")
for letra in frase:
    print(letra)

# Dada una cadena de caracteres, deseo contar cuantos de ellos son digitos
# (caracteres : .0,1,2,...9)

Parrafo_JRR = """Pero 2026 estamos justamente en el mundo de la literatura, es decir, de la probabilidad.
Todo reside en que el lector crea lo que le cuento. Y este es asunto mío. Bueno, Pedro
divide a los amantes en el Uno y el Dos y en el Tres y el Cuatro. Mediante cartas anónimas
o llamadas telefónicas u otros medios revela al Uno la existencia del Dos y al Tres la
existencia del Cuatro. Todo ello mediante una estrategia gradual y una técnica de la perfidia
que le permiten despertar en el 1308 agente escogido no solo los celos más atroces sino un
violento deseo de aniquilar al rival. Me olvidaba decirles que los amantes de Rosa, así
llamaremos a la mujer, estaban ferozmente enamorados de ella, se creían los únicos
depositarios de su amor y por 666 lo tanto la revelación de la existencia de competidores los
ofusca tanto como a Pedro mismo."""

# Inicializamos el contador
contador_dig = 0

# Utilizamos una estructura repetitiva para barrer todos los caracteres
# que componen a la variable de tipo str : Parrafo_JRR
for p in Parrafo_JRR:
    if p.isdigit():
        contador_dig = contador_dig + 1

print("El numero de digitos es : %d" %(contador_dig))

# Otra forma

# Acumulamos el numero de veces que aparece cada caracter de "0123456789"
count_dig = 0

for e in "0123456789":
    numero_dig_e = Parrafo_JRR.count(e)
    count_dig = count_dig + numero_dig_e

print("El numero de digitos es  : %d" %(count_dig))

# Ejemplito
# Dado un numero de elementos proveidos por el usuario,
# calcular la media geometrica de esos elementos
# (tambien proveidos por el usuario)

# Entradas/INPUTS

# Numero de elementos
n = int(input("Ingresa el numero de elementos a considerar : "))

# Definir una variable acumuladora : Para almacenar la productoria
# de los elementos proveidos por el usuario
productoria = 1

# Pidamos al usuario que ingrese esos n elementos y vamos acumulando
# el producto de ellos
for _ in range(n):
    num = float(input("Ingresa el valor : "))
    productoria = productoria * num

# OUTPUT : Calculamos la media geometrica
media_geom = productoria**(1/n)
print("Para los %d ingresados, la MG es : %.3f" %(n, media_geom))

# Casos a considerar mas a detalle
    # n = 0
    # Si n es par (impar), la productoria debe ser no positiva
    # otro caso
    # otro caso


# Otro Ejemplito
# Generemos 2026 numeros pseudoaleatorios en [0,1[ usando el modulo random .
# El objetivo es contar cuantos son menores o iguales a 0.5

# Cargar modulos
import random as rnd

# Variable contador : cuenta los numeros generados <= 0.5
num_veces = 0

# Deseo repetir/realizar un total de 2026 veces una determinada tarea
for p in range(2026):
    # Generamos un numero pseudoaleatorio
    numero_random = rnd.random()
    # Validamos una condicion sobre este numero pseudoaleatorio generado
    if numero_random <= 0.5:
        num_veces = num_veces + 1

# Mostremos el resultado
print("NUmero de veces que genero numeros <= 0.5 -> " , num_veces)
