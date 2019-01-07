#Escriba un subprograma en Python que determine si dos valores enteros dados son iguales o si su suma o diferencia es
# 5

def igualdad_a_cinco(a,b):
    """int,int --> bool
       OBJ: Comprueba si dos enteros son iguales o suma o diferencia es 5"""
    import math
    return (a == b) or (abs(a-b) == 5) or (a+b == 5)


#Programa que pide 5 mediciones de temperatura y un umbral y dice cuántas hay por encima de dicho umbral

NUM_VALORES = 5
umbral = float(input('Introduzca el valor umbral de temperatura: '))
por_encima = 0
for i in range(NUM_VALORES):
    temp = float(input('Introduzca una medición de temperatura: '))
    if temp > umbral:
        por_encima += 1
print('De las temperaturas dadas, ',por_encima, ' están sobre el umbral')


#Escriba una función en Python que sume 3 números y retorne el resultado, excepto en el caso de que dos o más de ellos
#sean iguales, en cuyo caso devolverá cero

def igualdad_a_tres(a,b,c):
    """ float, float, float --> float
    OBJ: suma 3 números, si dos o más de ellos son iguales retorna cero  """
    if (a==b) or (a==c) or (b==c): return 0
    else: return a+b+c


#Escribir un programa que calcule el número de pares e impares de una serie de números que se introducen por teclado
# (el usuario va introduciendo números hasta que con el centinela -999 indica que no quiere continuar)

def es_par(n):
    """ int --> bool
    OBJ: Determina si un entero es par """
    return n % 2 == 0
# Prueba
CENTINELA = -1
print("Entre un número entero, para salir introduzca ", CENTINELA, ": ",end='')
numero = int(input())
impares = 0
pares = 0
while (numero != CENTINELA):
  if es_par(numero): pares += 1
  else: impares += 1
  print("Entre un número entero, para salir introduzca ", CENTINELA, ": ",end='')
  numero = int(input())
if pares + impares > 0:
   print ("El número de pares encontrado es: " , pares)
   print ("El número de impares encontrado es: " , impares)