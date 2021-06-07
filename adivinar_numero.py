# -*- coding: utf-8 -*-
'''
Intenta adivinar un numero elegido de forma random por la
libreria random, entre 0 y 50.
Cuando se logra adivinar que numero es, se retorna el numero de intentos
'''

import random



def run():
    number_found = False
    random_number = random.randint(0, 50)
    intentos = 0
    
    while not number_found:
        number = int(raw_input('Intenta un número: '))
        intentos = intentos + 1
        
        if number == random_number:
            print('Felicidades. Encontraste el número en {} intentos'.format(intentos))
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')

if __name__ == "__main__":
    run()