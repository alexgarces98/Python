def obtenerPrecio(tipo,peso):
    '''string, float --> float
       OBJ: Da precios, introduciendo su precio y nombre
       PRE: tipo: platanos,peras,mandarinas o caquis'''
    if (tipo == 'Pera'):
        precio = 1.5
        resultado = precio * peso
    elif (tipo == 'Mandarina'):
        precio = 2.99
        resultado = precio * peso
    elif (tipo == 'Platano'):
        precio = 0.99
        resultado = precio * peso
    elif (tipo == 'Caqui'):
        precio = 1.75
        resultado = precio * peso

    return resultado


##PRUEBA:
print('PRUEBA 1: ',obtenerPrecio('Pera',2))
print('PRUEBA 2: ',obtenerPrecio('Mandarina',2))
print('PRUEBA 3: ',obtenerPrecio('Platano',2))
print('PRUEBA 4: ',obtenerPrecio('Caqui',2))



try:
    a = str(input('Introduzca la fruta que necesite (Mandarina, Platano, Pera, Caqui): '))
    b = float(input('Introduzca el peso de la fruta : '))
except:
    print('ERROR: Los datos introducidos son incorrectos')
else:
    print('La fruta que ha seleccionado es: ',a,' y su peso es: ',b,' ,por lo que le costara comprarla: ',obtenerPrecio(a,b))



