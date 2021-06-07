# -*- coding: utf-8 -*-
'''
Una forma de sumar numeros sin usar el operador '+' directamente
'''


def suma_recursiva(primer_numero, segundo_numero):
    print(segundo_numero)

    if primer_numero == 0:
        return segundo_numero
    else:        
        return suma_recursiva(primer_numero - 1, segundo_numero + 1)
        



def run():
    primer_numero = int(raw_input('Ingrese el primer número: '))
    segundo_numero = int(raw_input('Ingrese el número que desea sumar con {}: '.format(primer_numero)))
    resultado = suma_recursiva(primer_numero, segundo_numero)
    print('El resultado de sumar {} con {} es : {}'.format(primer_numero, segundo_numero, resultado ))


if __name__ == "__main__":
    print('B I E N V E N I D O A   L A   S U M A   R E C U R S I V A')
    run()