# Definicion
t1 = ()
t2 = (12,34,56,78,"AAA", "19")
t3 = ([], [12,45], True, list(), [1 for i in range(5)])

# Tipo de dato
type(t1)

# Tipo de dato
type(t2)

# Tipo de dato
type(t3)

# Los datos de tipo tupla son inmutables
t2[2] ="666"

# Al igual que con str y list , las tuplas se pueden concatenar y repetir
t4 = t2 + t3
t5 = 15*t3

# tipode dato
type(t4)

# tipode dato
type(t5)

dir(t1)

# # Los metodos de interes :
#  'count',
#  'index'
