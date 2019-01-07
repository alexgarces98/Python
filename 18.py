# Archivo:18.py
# Autor: Alejandro García 
# Fecha: 8/10/2018
# Descripción: Escribe un programa que lea un entero positivo n y genere:
#a. una tabla con las n primeras potencias de 2.
#b. una tabla con las potencias de 2 que son menores o iguales que n.

exponente = int(input("Introduce un entero para realizar las potencias de 2: "))

for exponente in range (0, exponente):
    print (2 ** exponente)

n =  2

while n <= exponente:
    n = n * 2
    print ("Todos las potencias de 2 menores o iguales que n son: ",n)


