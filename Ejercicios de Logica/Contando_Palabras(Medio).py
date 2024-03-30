"""
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
"""


def Contador(palabra):
    lista = palabra.split()
    diccionario = {}

    for i in lista:
        if i in diccionario:
            diccionario[i] +=1
        else:
            diccionario[i] = 1
    
    for i,x in diccionario.items():
        print(f"{i} : {x}")

Contador("hola que tal hola")