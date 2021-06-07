# -*- coding: utf-8 -*-

'''
Una palabra palindroma se escribe al derecho y al revés, sin perder si significado.
esta pieza de codigo nos ayuda a identificar si es palindroma o no.
'''


def es_palindromo(palabra):
    palabra_invertida = palabra[::-1]    

    if palabra_invertida == palabra:
        return True
    else:
        return False


def run():
    palabra = str(raw_input('Ingrese una palabra: '))
    resultado = es_palindromo(palabra)
    
    if resultado:
        print('La palabra ingresada es palíndroma')
    else:
        print('La palabra ingresada no es palídroma')


if __name__ == "__main__":
    run() 