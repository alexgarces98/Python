def sumar(n1, n2, n3):
    '''int,int,int --> int
       OBJ: Suma 3 numeros y si 2 de ellos o mas son iguales devuelve 0
       PRE: si n1==n2 or n1 == n3 or n2 == n3      return 0'''
    if (n1 != n2) and (n1 != n3) and (n2 != n3):
        suma = n1 + n2 + n3
    else:
        suma = 0
    return suma


##PRUEBA:
print('PRUEBA 1: ', sumar(1, 2, 3))
print('PRUEBA 2: ', sumar(1, 1, 3))
print('PRUEBA 3: ', sumar(1, 2, 1))
print('PRUEBA 4: ', sumar(1, 2, 2))
print('PRUEBA 5: ', sumar(-1, -2, 3))

try:
    x = int(input('Introduce el primer numero entero: '))
    y = int(input('Introduce el segundo numero entero: '))
    z = int(input('Introduce el tercer numero entero: '))
except:
    print('ERROR: El dato que intento introducir no es correcto, por favor vuelvalo a intentar')
else:
    print('La suma de los numeros es : ', sumar(x, y, z))
