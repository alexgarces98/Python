# Archivo: 3.py
# Autor: Alejandro García
# Fecha: 30/11/2018
# Descripción: Muy similar al anterior: Programar ahora un algoritmo recursivo que permita
# hacer una división entera mediante restas sucesivas.


def dividir(dividendo, divisor):
    contador = 0
    dividendo = dividendo - divisor;

    while (dividendo >= 0):
        contador = contador + 1
        dividendo = dividendo - divisor

    return str(contador)

print(dividir(6, 3))
