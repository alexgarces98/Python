# Archivo: 8.py
# Autor: Alejandro García
# Fecha: 30/11/2018
# Descripción: Calcular la suma de los números pares entre 0 y n de manera recursiva.

def sumarNumPares (n):
    if (n == 0):
        return 0
    else:
        return n + sumarNumPares(n-2)

n = int(input("Ingresar la cantidad de terminos pares para sumar: "))
print("La suma de los primeros numeros pares es de: " + str(sumarNumPares(n*2)))

