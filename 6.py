# Archivo: 6.py
# Autor: Alejandro García
# Fecha: 30/11/2018
# Descripción: Realizar una función recursiva que dado un número entero, cuente su número
# de dígitos.

def contarDigitos(n):
    if n < 10:
        return 1
    else:
        return 1 + contarDigitos(n/10)

print(contarDigitos(5))