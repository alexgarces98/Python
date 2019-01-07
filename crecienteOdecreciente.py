#Programa que lea por teclado una serie de 10 números enteros e indique si los números están ordenados de forma
#creciente, si lo están de forma decreciente, o si por el contrario están desordenados.

creciente = True
decreciente = True
anterior = int(input("Introduce un número de la serie: "))
for i in range (10):
    x = int(input("Introduce un número de la serie: "))
    if x >= anterior:
        decreciente = False
    elif x <= anterior:
        creciente = False
    anterior = x

if decreciente:
     print("La serie es decreciente")
elif creciente:
     print("La serie es creciente")
else:
     print("La serie está desordenada")