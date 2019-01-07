# Archivo:16.py
# Autor: Alejandro García 
# Fecha: 8/10/2018
# Descripción: Escribe un programa que pida un número límite y calcule cuántos 
#términos de la serie armónica son necesarios para que su suma supere dicho 
#límite. Es decir, dado un límite introducido por el usuario (por ejemplo 50) 
#se trata de determinar el menor número n tal que:

#1 + 1/2 + 1/3 + ... + 1/n > límite

#En nuestro ejemplo, para un límite = 5, n sería 83. El programa ha de ser 
#robusto, es decir, ha de controlar que el número introducido por el usuario 
#es un entero positivo.

def armonin(n):
    if n >= 1:
        suma = 0.0
        i = 1.0
        while i <= n:
            suma = suma + 1/i
            print("Suma", suma)
            i = i+1
        return suma
    else:
        print ("Valor no permitido")
        return

def serie(p, n):
    if n >=1:
        suma = 0.0
        i = 1.0
        while i <=n:
            suma = suma + 1/i**p
            print ("Suma: ", suma)
            i = i+1
        return suma
    else:
        print("Valor no permitido: ")
        return -1

n = int(input("Ingrese numero de iteraciones: "))
if n >= 1:
    print ("SUMAS: ", armonin(n))
else:
    print(" ", armonin(n))
print ("Serie P con p = 2")

n = input("Ingrese numero de iteraciones: ")
if n >=1:
    print("SUMAS: ", serie(2, n))
else:
    print (" ", serie(2, n))

