# Para mostrar dos variables como error1 y error2 : utilicemos dos print
print(error1)
print(error2)

# Seamos mas explicitos al momento de mostrar los resultados
print("El error cometido por mi aprox. de taylor ", error1 )
print("El error cometido por la funcion seno del modulo math es  : ", error2)

# Podemos meter toda esta informacion en un print
# (utilizando el caracter salto de linea : \n)
print("El error cometido por mi aprox. de taylor ", error1 , "\nEl error cometido por la funcion seno del modulo math es  : ", error2)

# Ejemplito
# Calculemos el interes simple de un monto proveido por el usuario (M0) a una
# tasa (i) del 10% anual con un horizonte (t) dado por el usuario

# Inputs
M0 = float(input("Ingresa el monto inicial : "))
t = float(input("Inigresa el tiempo (resolucion anual) : "))

# Operaciones (Teorico)
i = 0.1
interes = M0 * i * t

# Salida/Outputs
print("El interes generado es: " , interes)
print("El interes generado es %.2f" %(interes))

# Otra forma  : docstring
print("""
Calculadora de Interes
----------------------

    Monto Inicial : %.2f
    Tiempo : %.2f
    ====================

    Interes generado  : %.2f

""" %(M0, t , interes))
