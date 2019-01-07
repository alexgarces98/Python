# Archivo:14.py
# Autor: Alejandro García 
# Fecha: 8/10/2018
# Descripción: Escribe un programa que lea una serie de números enteros hasta 
#que se introduzca el número -9999, y cuente el total de números introducidos, 
#el total de valores positivos y el total de valores negativos (no consideres 
#el cero ni positivo ni negativo). Reutilizar la función del ejercicio 9 para 
#validar tus entradas.

dato = 0
positivos = 0
negativos = 0

while dato != -9999:

    dato = int(input("Ingresa un numero natural: "))

    if dato > 0:
        positivos += 1

    elif dato < 0:
        negativos += 1

print ("La cantidad de numeros positivos: ", positivos,
        "\nLa cantidad de numeros negativos fue: ", negativos)
