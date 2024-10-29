# SOMBRERO SELECCIONADOR: 

#Este es el último añadido, me he calentado y le voy a meter un bucle:

Bucle = 'Si'  # Inicializamos en "Si" para entrar en el bucle la primera vez.
while Bucle == 'Si':

    # Voy a empezar con mis variables, despuésformular las preguntas y asignar las puntuaciones. 

    Gryffindor = 0
    Ravenclaw = 0
    Hufflepuff = 0
    Slytherin = 0


    #PREGUNTA 1

    Dia = int(input(
        "¿Qué prefieres? \n"
        " 1: Amanecer \n"
        " 2: Atardecer \n Respuesta: " ))
    if Dia == 1:
        Gryffindor += 1
        Hufflepuff += 1

    elif Dia == 2:
        Ravenclaw += 1
        Slytherin += 1
    else:
        print('Dato erróneo, cambia de hechizo.')

    # Estos prints('\n') simplemente son para que en la consola aparezcan espacios y nos e junten a tope el texto. 
    print('\n')

    # PREGUNTA 2

    Muerte = int(input('Cuando muera, quiero ser recordado como: \n 1: El buenazo. \n 2: El listillo. \n '
                       '3: El rancio. \n 4: ¿Quíen dijo muerte?... MUAJAJAJA. \n Respuesta: '))
    if Muerte == 1:
        Gryffindor += 2
    elif Muerte == 2:
        Ravenclaw += 2
    elif Muerte == 3:
       Hufflepuff += 2
    elif Muerte == 4:
        Slytherin += 2
    else:
        print('Dato erróneo, cambia de hechizo.')

    print('\n')
    # PREGUNTA 3

    Animal = int(input('¿Cuál es tu animal favorito? \n 1: El peluuuca. \n 2: El PPN (versión black del PPM). \n'
                        ' 3: La rata gigante vaga del subsuelo. \n 4: El que más mate, que tóxicooo. \n Respuesta: '))
    if Animal == 1: 
        Gryffindor += 2
    elif Animal == 2:
        Ravenclaw += 2
    elif Animal == 3:
        Hufflepuff += 2
    elif Animal == 4:
        Slytherin += 2
    else:
        print('Dato erróneo, cambia de hechizo.')

    print('\n')

    # De esta manera puedo ir comprobando si voy haciendo bien el código al final, voy a ir escribiendo por encima de esto así que 
    # cuando el código esté comentario no va a tener ningún sentido.

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
    print('Gryffindor= ', Gryffindor)
    print('Ravenclaw = ', Ravenclaw)
    print('Hufflepuff = ', Hufflepuff)
    print('Slytherin = ', Slytherin)

    Bucle = input('¿Quieres volver a probar? (Si/No): ')

print("Gracias por participar!!")


# HAY PROBLEMAS, UNO QUE SE PUEDE HACER MUCHO MÁS SIMPLIFICADO, MIRAR EL CODEDEX, DOS, QUE COMO SOLO VALE UN PUNTO Y HAY POCAS PREGUNTAS 
# ES DEMASIADO FACIL EMPATAR EN PUNTOS Y QUE NO DECLARE QUE SEAS DE NINGUNA CASA, QUE NO ROMPE EL PROGRAMA, PERO SE SALTA ESA PARTE. 

#mejorar con funciones += y con la función max() para simplificar mucho el proceso. 