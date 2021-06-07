# -*- coding: utf-8 -*-
'''
Uso de diccionarios.
Los diccionarios son una estructura de control que consta de una llave y un valor. En este ejemplo
se puede ver como almacenan y se accede a ellos.
ejm: llaves: mexico, colombia, argentina y perú
Valores: su cantidad de habitantes'''




countries = {
    'mexico' : '122 millones',
    'colombia' : '49 millones',
    'argentina' : '42 millones',
    'perú' : '22 millones'
}
while True:    
    country = str(raw_input('Ingrese un país: ')).lower()
    
    try:
        print('El país {} tiene {} de habitantes').format(country, countries[country])
    except KeyError:
        print('No tenemos datos del país {}'.format(country))  
