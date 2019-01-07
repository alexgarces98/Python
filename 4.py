# Archivo: 4.py
# Autor: Alejandro García
# Fecha: 30/11/2018
# Descripción: Programar, haciendo uso de la recursividad, una función en Python que
# permita obtener el término de orden n de la sucesión de Fibonacci

def fibonacci(n):
    if (n == 1 or n == 2 ):
        return 1
    else:
        suma = fibonacci(n-2) + fibonacci(n-1)
        return suma

print(fibonacci(56))