# Archivo: 10.py
# Autor: Alejandro García
# Fecha: 30/11/2018
# Descripción: Dado un número en base decimal y una base menor que diez, escribir un
# programa que cambie dicho número a la base dada utilizando para ello un
# procedimiento recursivo.

'''def cambiar_base(numero, base):


cambiar_base(56, 2)'''


def convertirDecimal(n, base):
    """ Cambia n de base
     REQ: base < 10"""
    if n < base:
        return str(n)
    else:
        return convertirDecimal(n//base, base) + str(n % base)



print(convertirDecimal(5, 2))
print(convertirDecimal(14, 4))