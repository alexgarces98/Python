CENTINELA = -1
try:
    print("Entre un número, para salir introduzca ", CENTINELA, ": ", end='')
    numero = int(input())
    mayor = menor = numero
    total = 0
    cantidad_numeros = 0
    while (numero != CENTINELA):
        total += numero
        cantidad_numeros += 1
        if numero > mayor: mayor = numero
        if numero < mayor: menor = numero
        print("Entre un número, para salir introduzca ", CENTINELA, ": ", end='')
        numero = int(input())
    if cantidad_numeros > 0:
        print("La media es: ", total / cantidad_numeros)
        print("El mayor es: ", mayor, ", y el menor numero es: ", menor)
except:
    print("Error, debe introducir un numero valido")