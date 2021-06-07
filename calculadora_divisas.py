# -*- coding: utf-8 -*-
'''
calculadora de divisas básica, en este caso de pesos MEX a pesos COP
se puede comvertir cualquier moneda, ajustando la variable 'mex_to_col_rate',
al valor actual de cambio o simplemente creando otra variable y usandola en la
linea 12
'''

def foreing_exchance_calculator(ammount):
    mex_to_col_rate = 145.97

    return mex_to_col_rate * ammount

def run():
    print('C A L C U LA D O R A D E D I V I S A S')
    print('Convierte pesos mexicanos a pesos colombianos.')
    print('')

    ammount = float(raw_input('Ingresa la cantidad de pesos mexicanos que quieres convertir: '))

    result = foreing_exchance_calculator(ammount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(ammount, result))
    print('')

if __name__ == '__main__':
    run()