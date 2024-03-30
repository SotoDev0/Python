"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un anagrama es una palabra o frase formada reorganizando 
     las letras de otra palabra o frase.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""


def is_anagram(str1,str2):
    # Convertir las palabras a minúsculas y ordenar los caracteres
    palabra1 = sorted(str1.lower())
    palabra2 = sorted(str2.lower())

    # Verificar si las palabras ordenadas son iguales
    if palabra1 == palabra2:
        return False  # Las palabras son idénticas, no son anagramas
    else:
        return True   # Las palabras son diferentes, podrían ser anagramas


print(is_anagram("ala","ala"))