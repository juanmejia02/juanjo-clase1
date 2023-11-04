# contador = 10
# while contador >= 1:
#     print(f"valor del contador: {contador}")
#     contador = contador -1
    
# acendente = 0
# decendente = 11
# while acendente < 10:
#         acendente += 1
#         decendente -= 1
#         print(acendente, '/', decendent 
    
import random

aleatoreo = random.randint(1, 100)
adivina = 0
 
while adivina != aleatoreo:
    if adivina == 0:
         print('Inicia el juego')
    elif adivina < aleatoreo:
        print('demasiado bajo')
    else:
        print('demasiado alto')
    adivina = int(input('Ingresa el numero'))
print('haz ganado!!!')
    
    