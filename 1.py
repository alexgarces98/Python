# Archivo:1.py
# Autor: Alejandro García
# Fecha: 30/11/2018
# Descripción: Programar un procedimiento recursivo que compruebe si un cierto número se encuentra o no en una lista.

def comprobar(x, num, i = 0):
    if i >= len(x):
        return False
    elif x[i] == num:
        return True
    else:
        return comprobar(x, num, i + 1)

print(comprobar(4,5,0))
