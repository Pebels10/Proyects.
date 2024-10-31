

import random

def tirar_dado():
    while True:
        afirmativo = input('¿Quieres tirar el dado? (si/no) ').lower()
        
        if afirmativo == 'si':
            print('¡Suerte!')
            break
        elif afirmativo == 'no':
            print('¡Sigue maquinando!')
            return  # Salir de la función si el usuario no quiere tirar
        else:
            print('Por favor, responde con "si" o "no".')

    # Obtener ventaja y lanzar el dado
    ventaja = int(input('¿Qué ventaja tienes? '))
    num = random.randint(1, 20)

    if num + ventaja >= 10 and num != 20 and num != 1:
        print('¡Acierto!')
    elif num == 1:
        print('Pifia...')
    elif num == 20:
        print('¡Crítico!')
    else:
        print('¡Fallo!')

    print(num, '+', ventaja, '=', num + ventaja)

# Bucle principal
while True:
    tirar_dado()
    volver_a_jugar = input('¿Quieres volver a jugar? (Si/No): ').lower()
    if volver_a_jugar != 'si':
        print('¡Vuelve a jugar cuando quieras!')
        break