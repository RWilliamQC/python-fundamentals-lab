# Definamos algunas variables de tipo str
cad1 = "PIT705 Python Basico"
cad2 = "Abraham Zamudio"
cad3 = "El peor curso de mi vida"

# Concatenar variables de tipo str : +
cad4 = cad1 + "-" + cad2
cad5 = 44*cad3

# Lista de metodos/atributos de una str
dir(cad4)

# Funcion help
help("".capitalize)

# Ejemplito
"pit705".capitalize()

# Veamos la documentacion del metodo : isalnum
help(cad6.isalnum)

# Ejemplito
"".isalnum()

# Ejemplito
"666PIT".isalnum()

cad10 = """El colchonero con su larga pértiga de membrillo sobre el hombro y el rostro recubierto de polvo y de pelusas atravesó el corredor de la casa de vecindad, limpiándose el sudor con el dorso de la mano. —¡Paulina, el té! —exclamó al entrar a su habitación dirigiéndose a una muchacha que, inclinada sobre un cajón, escribía en un cuaderno. Luego se desplomó en su catre. Se hallaba extenuado. Toda la mañana estuvo sacudiendo con la vara un cerro de lana sucia para rehacer los colchones de la familia Enríquez. A mediodía, en la chingana de la esquina, comió su cebiche y su plato de frejoles y prosiguió por la tarde su tarea. Nunca, como ese día, se había agotado tanto. Antes del atardecer suspendió su trabajo y emprendió el regreso a su casa, vagamenre preocupado y descontento, pensando casi con necesidad en su catre destartalado y en su taza de té. —Acá lo tienes —dijo su hija, alcanzándole un pequeño jarro de metal—. Está bien caliente —y regresó al cajón donde prosiguió su escritura. El colchonero bebió un sorbo mientras observaba las trenzas negras de Paulina y su espalda tenazmente curvada. Un sentimiento de ternura y de tristeza lo conmovió. Paulina era lo único que le quedaba de su breve familia. Su mujer hacía más de un año que muriera víctima de la tuberculosis. Esta enfermedad parecía ser una tara familiar, pues su hijo que trabajaba de albañil, falleció de lo mismo algún tiempo después. """
type(cad10)
len(cad10)
help("".count)
# Ejemplito : Contemos el numero de espacios en blanco que hay cad10
cad10.count(" ")
