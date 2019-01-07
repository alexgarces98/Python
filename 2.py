# Archivo: 2.py
# Autor: Alejandro García
# Fecha: 30/11/2018
# Descripción: Implementar un programa que dados dos números, calcule el producto de forma recursiva. Los números a
# multiplicar deben ser leídos por teclado.
# NOTA: no puede utilizar el operador de multiplicación así que utilice sumas.

def multiplicarNumeros(x, y):
    if y < 0:
        return -multiplicarNumeros(x, -y)
    elif y == 0:
        return 0
    elif y == 1:
        return x
    else:
        return x + multiplicarNumeros(x, y - 1)

print(multiplicarNumeros(3, 5))