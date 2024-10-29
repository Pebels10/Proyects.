# SOMBRERO SELECCIONADOR: 

# Voy a empezar a formulando las preguntas y las puntuaciones. 

#PREGUNTA 1

Dia = int(input(
    "¿Qué prefieres? \n"
    " 1: Amanecer \n"
    " 2: Atardecer \n Respuesta: " ))
if Dia == 1:
    g1, h1 = 1, 1
    r1, s1 = 0, 0

else:
    r1, s1 = 1, 1
    g1, h1 = 0, 0

# Estos prints('\n') simplemente son para que en la consola aparezcan espacios y nos e junten a tope el texto. 
print('\n')

# PREGUNTA 2

Muerte = int(input('Cuando muera, quiero ser recordado como: \n 1: El buenazo. \n 2: El listillo. \n 3: El rancio. \n 4: ¿Quíen dijo muerte?... MUAJAJAJA. \n Respuesta: '))
if Muerte == 1:
    g2 = 1
    r2, h2, s2 = 0, 0, 0
elif Muerte == 2:
    r2 = 1
    g2, h2, s2 = 0, 0, 0 
elif Muerte == 3:
    h2 = 1
    g2,r2, s2 = 0, 0, 0
else:
    s2 = 1
    g2, r2, h2 = 0, 0, 0

print('\n')
# PREGUNTA 3

Animal = int(input('¿Cuál es tu animal favorito? \n 1: El peluuuca. \n 2: El PPN (versión black del PPM). \n'
                    ' 3: La rata gigante vaga del subsuelo. \n 4: El que más mate, que tóxicooo. \n Respuesta: '))
if Animal == 1: 
    g3 = 1
    r3, h3, s3 = 0, 0, 0
elif Animal == 2:
    r3 = 1
    g3, h3, s3 = 0, 0, 0
elif Animal == 3:
    h3 = 1
    g3, r3, s3 = 0, 0, 0
else:
    s3 =1
    g3, r3, h3 = 0, 0, 0

print('\n')

# De esta manera puedo ir comprobando si voy haciendo bien el código al final, voy a ir escribiendo por encima de esto así que 
# cuando el código esté comentario no va a tener ningún sentido.

Gryffindor = g1 + g2 + g3
Ravenclaw = r1 + r2 + r3
Hufflepuff = h1 + h2 + h3
Slytherin = s1 + s2 + s3

if Gryffindor > Ravenclaw and Gryffindor > Hufflepuff and Gryffindor > Slytherin:
    print('Bienvenido a Gryffindor!! 🦁')
elif Ravenclaw > Gryffindor and Ravenclaw > Hufflepuff and Ravenclaw > Slytherin:
    print('Bienvenido a Ravenclaw!! 🐧')
elif Hufflepuff > Gryffindor and Hufflepuff > Ravenclaw and Hufflepuff > Slytherin:
    print('Bienvenido a Hufflepuff! 🦡')
elif Slytherin > Gryffindor and Slytherin > Ravenclaw and Slytherin > Hufflepuff:
    print('Bienvenido a Slytherin! 🐍')

print('\n')

print('Tu afinidad en Howarts es...')
print("Gryffindor = ", g1 + g2 + g3)
print('Ravenclaw = ', r1 + r2 + r3)
print('Hufflepuff = ', h1 + h2 + h3)
print('Slytherin = ', s1 + s2 + s3)

# HAY PROBLEMAS, UNO QUE SE PUEDE HACER MUCHO MÁS SIMPLIFICADO, MIRAR EL CODEDEX, DOS, QUE COMO SOLO VALE UN PUNTO Y HAY POCAS PREGUNTAS 
# ES DEMASIADO FACIL EMPATAR EN PUNTOS Y QUE NO DECLARE QUE SEAS DE NINGUNA CASA, QUE NO ROMPE EL PROGRAMA, PERO SE SALTA ESA PARTE. 

#mejorar con funciones += y con la función max() para simplificar mucho el proceso. 