# Ejemplito
# Consideremos pedir al usuario su edad (almacenada en memoria ram como un int)
# En funcion del valore ingresado, tomaremos algunas acciones :
    # edad >= 0 y edad<18 : "Es momento de preparar el terreno para la siembra"
    # edad >=18 y edad<29 : "Es momento de sembrar"
    # edad >= 29 y edad < 45 : "Es momento de cuidar el terreno para futuras siembras"
    # edad >= 45 y edad < 99 : "Es momento de disfrutar la cosecha"

print("Bienvenidos a mi primera celda que utiliza la estructura de decision IF")

# Entradas/Inputs
edad_user = int(input("Ingresa tu edad (Numero Entero) : "))

# Implementemos la logica
if (edad_user >= 0 ) and (edad_user < 18):
    print("Es momento de preparar el terreno para la siembra")
elif (edad_user >= 18) and (edad_user < 29):
    print("Es momento de sembrar")
elif (edad_user >= 29) and (edad_user < 45):
    print("Es momento de cuidar el terreno para futuras siembras")
elif (edad_user >= 45) and (edad_user < 99) :
    print("Es momento de disfrutar la cosecha")
else:
    print("El valor ingresado no es una edad adecuada (considerada)")


# Primer escenario


print("Bienvenidos a mi primera celda que utiliza la estructura de decision IF")

# Entradas/Inputs
#
# ==============================================================================
# edad_user = int(input("Ingresa tu edad (Numero Entero) : "))
# ==============================================================================
edad_user = input("Ingresa tu edad (Numero Entero) : ")
if edad_user.isdigit():
    edad_user = int(edad_user)

    # Implementemos la logica
    if (edad_user >= 0 ) and (edad_user < 18):
        print("Es momento de preparar el terreno para la siembra")
    elif (edad_user >= 18) and (edad_user < 29):
        print("Es momento de sembrar")
    elif (edad_user >= 29) and (edad_user < 45):
        print("Es momento de cuidar el terreno para futuras siembras")
    elif (edad_user >= 45) and (edad_user < 99) :
        print("Es momento de disfrutar la cosecha")
    else:
        print("El valor ingresado no es una edad adecuada (considerada)")

else:
    print("Ingreso ERRONEO")
