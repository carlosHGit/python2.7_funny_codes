# -*- coding: utf-8 -*-
'''
algoritmo recursivo para buscar un elemento en una lista de objetos, no se comparan uno por uno
los elementos si no que se va dividiendo cada vez en dos grupos, hasta que se llega a la mínima
comparacion y entonces retorna si el valor se encuentra o no en la lista, sin ocupar muchos recursos
de la pc
'''


def binary_search(numbers, number_to_find, low, high):

    if low > high:
        return False
    
    mid = (low + high) / 2

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid -1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 21, 22 ,32 ,33 ,54 , 55]

    number_to_find = int(raw_input('Ingrese un número'))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print('El número sí está en la lista.')
    else:
        print('El número NO está en la lista')