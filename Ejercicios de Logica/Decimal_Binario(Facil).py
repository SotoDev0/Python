"""
 * Crea un programa se encargue de transformar un número
 * decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.
"""


def binario(number):
    B = []

    while number != 0:
        B.append(number%2)
        number //= 2
    
    return B[::-1]



print(binario(29))