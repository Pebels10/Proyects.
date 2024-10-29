# DADO DE ROL D20 V 2.0 (ELIF + ELSE)+ MIERDA DE BUCLES ME LO HE CARGADO Y NO SE COMO. 

# Primera parte: Se designa un programilla para saber si quieres tirar el dado o no. Una especie de START. 
Bucle = 'Si'
while Bucle == 'Si':
    print('Adelante!') 

  #Es un bucle para que te siga preguntando lo mismo hasta que se cumpla una condición que lo rompa. 
    afirmativo = ('Si')
    while afirmativo == 'Si':
      afirmativo = input('Quieres tirar el dado? (Si/No) ')
      if afirmativo == 'Si':
        print('Suerte!')
      else:
        print( 'Sigue maquinando!!')
        break

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

    bucle = input('¿Quieres volver a jugar? (Si/No): ')
    if bucle == 'No':
      break

print('Vuelve a jugar cuando quieras!')


