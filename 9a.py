# Archivo:9a.py
# Autor: Alejandro García
# Fecha: 24/11/2018
# Descripción: Implemente una función que indique si una palabra contiene las cinco vocales: por ejemplo “murciélago”.
# Modifique posteriormente la función para que detecte sólo aquellas palabras que contienen una única vez cada vocal.

vocales = ["a","e","i","o","u"]
encontradas = []
word = input("Introduce la palabra que quieras comprobar: ")


def contiene_cinco_vocales(palabra):
    for letra in word:
        if letra in vocales:
            if letra not in encontradas:
                encontradas.append(letra)
    for vocal in encontradas:
        print(vocal)
    return palabra.upper().find("A") > -1 and palabra.upper().find("E") > -1 and palabra.upper().find("I") > -1 and \
           palabra.upper().find("O") > -1 and palabra.upper().find("U") > -1


if contiene_cinco_vocales(word) == True:
    print("La palabra contiene las 5 vocales")
else:
    print("La palabra no contiene las 5 vocales")

