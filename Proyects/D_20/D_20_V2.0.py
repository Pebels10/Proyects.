# DADO DE ROL D20 V 2.0 (ELIF + ELSE)

# Primera parte: Se designa un programilla para saber si quieres tirar el dado o no. Una especie de START. 

while True: #Es un bucle para que te siga preguntando lo mismo hasta que se cumpla una condición que lo rompa. 

  start = input('Quieres tirar el dado? (si/no) ')
  afirmativo = ('si')

  if start == afirmativo:
    print('Suerte!')
    break #Esto hace que salga del bucle infinito.

  else:
    print( 'Sigue maquinando!!')

# Segunda parte: Es el dado en sí. No entiendo muy bien ni el funcionamiento de import random ni el deranmom.randint.

import random

advantage = int(input('Qué ventaja tienes? '))

num = random.randint(1 , 20)  # Generates a random number that's either 0 or 1

if num + advantage >= 10 and num != 20 and num != 1:
  print('Acierto!')
  print(num , '+' , advantage , '=' , num + advantage)
elif num == 1:
  print('Pifia...')
  print(num , '+' , advantage , '=' , num + advantage )
elif num == 20:
  print('Crítico!')
  print(num , '+' , advantage , '=' , num + advantage)
else:
  print('Fallo!')
  print(num , '+' , advantage , '=' , num + advantage)

## quiero añadirle un ciclo para que cuando termine vuelva a empezar pero una opción al principio del todo que sea si/no/cerrar.
