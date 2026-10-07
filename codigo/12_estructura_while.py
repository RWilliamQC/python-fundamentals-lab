# Ejemplito : Calculo del epsilon de la computadora
# Un numero diferente de cero epsilon  : epsilon + 1 = 1

# Veamos una implementacion canonica

# inicilizamos el valor del epsilon
eps = 1.0

# Bucle while
while (eps + 1.0) != 1.0:
    eps = eps / 2.0

# Correccion final
epsilon_maquina = 2.0 * eps

# Mostremos el valor de epsilon_maquina y verifiquemos
print("Epsilon de la maquina ", epsilon_maquina)
print("Verificacion : %.3f"  %(float(epsilon_maquina + 1.0)))


# Rastreo del estado interno

# Inicializacion
eps = 1.0
ultimo_valor = eps
iteraciones = 0

# Bucle de seguimiento
while (eps + 1.0) != 1.0:
    ultimo_valor = eps
    # print(ultimo_valor)
    eps  = eps / 2.0
    iteraciones = iteraciones + 1

# Asignacion final
epsilon_maquina = ultimo_valor

# Mostremos el valor de epsilon_maquina y verifiquemos
print("Epsilon de la maquina ", epsilon_maquina)
print("Verificacion : %.16f"  %(float(epsilon_maquina + 1.0)))
print("Numero de iteraciones ", iteraciones)


# Ejemplito
# Pidamos al usuario una serie de numeros hasta que el usuario ingrese
# un numero menor a cero
# Calculemos la suma de esos numeros >= 0.

# Contemos el numero de veces que el usuario provee un numero >= 0
contador_positivos = 0

# Definamos la variable donde acumularemos la sumas de los numeros >= 0
suma_total = 0

# Mostremos un  mensaje intuitivo
print("Ingresa un numero menor a cero para terminar la ejecucion !!!")

# Pidamos al usuario el primer numero
numero = float(input("INgresa un numero : "))

# Estructura repetitiva while
while (numero>= 0):
    # almacenamos el numero
    contador_positivos  = contador_positivos +1
    # actualizamos la variable suma_total
    suma_total = suma_total + numero
    # pedimos nuevamente que el usuario ingrese un numero
    numero = float(input("Ingrese un numero "))

# Mostremos resultados
print("Suma total : ", suma_total)
print("Cantidad >= 0 ingresados : ", contador_positivos)
