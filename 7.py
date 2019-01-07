# Archivo: 7.py
# Autor: Alejandro García
# Fecha: 30/11/2018
# Descripción: Realizar un programa que lea desde teclado un número entero positivo y lo
# convierta a binario utilizando recursividad.


def convertirEnteroAbin(n):
    if n < 0:
        return 'Introduce un entero positivo'
    elif n == 0:
        return '0'
    else:
        return convertirEnteroAbin(n//2) + str(n%2)

print(convertirEnteroAbin(456))