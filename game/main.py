import random

#partidas = [1,2,3,4]

def elegir_opciones():
  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ')
  user_option= user_option.lower()
  
  if user_option not in options:
    print("Esa opción no es valida")
    # continue
    return None, None
  computer_option = random.choice(options)
  print("Opción del usuario =>",user_option)
  print("Opción del computador =>",computer_option)
  return user_option, computer_option
  
def reglas_juego(user_option, computer_option, puntuacion_usuario, puntuacion_computadora):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('Piedra gana a tijera')
      print('User gano!')
      puntuacion_usuario += 1

    else:
      print('Papel gana a piedra')
      print('Computer gano!')
      puntuacion_computadora += 1

  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('Papel gana a piedra')
      print('User gano!')
      puntuacion_usuario += 1

    else:
      print('Tijera gana a papel')
      print('Computer gano!')
      puntuacion_computadora += 1

  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('Tijera gana a papel')
      print('User gano!')
      puntuacion_usuario += 1

    else:
      print('Piedra gana a tijera')
      print('Computer gano!')
      puntuacion_computadora += 1
  return puntuacion_usuario, puntuacion_computadora

def check_winner(pepe, papa):
  if pepe == 2:
    print('EL USUARIO GANÓ LA PARTIDA')
    exit()
  if papa == 2:
    print('LA COMPUTADORA GANÓ LA PARTIDA')
    exit()
  

def correr_juego():
  puntuacion_usuario = 0
  puntuacion_computadora = 0
  rounds = 1
  while True:
    

    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    rounds += 1
  
    user_option, computer_option = elegir_opciones()
    puntuacion_usuario, puntuacion_computadora = reglas_juego(user_option, computer_option, puntuacion_usuario, puntuacion_computadora)
    check_winner(puntuacion_usuario, puntuacion_computadora)
    
      

    print(f'Puntuación usuario: {puntuacion_usuario}')
    print(f'Puntuación computadora: {puntuacion_computadora}')

correr_juego()