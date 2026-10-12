# Carguemos el modulo
import datetime

# Documentacion del modulo
help(datetime)

# De las primeras lineas de la documentacion del modulo datetime
fecha1 = datetime.date(1982, 3, 26)

# tipo de dato
type(fecha1)

# Definamos otra fecha
fecha2 = datetime.date(2026, 8, 18)

# Tipo de dato
type(fecha2)

# Calculemos la diferencia de dos objetos de tipo datetime.date
dt1 = fecha2 - fecha1

# Es muy natural concebir el hecho de que el objeto dt1  no sea un datetime.date
# Tipo de dato
type(dt1)

# Veamos que valor almacena la variable (u objeto) : dt1
dt1

# Utilicemos la funcion print
print(dt1)

# LIstar los metodos/atributos que puedo aplicar a un dato de tipo datetime.timedelta
dir(dt1)

# Documentacion
help(dt1.days)

dt1.days

# Numero de años (aprox)
dt1.days/365
