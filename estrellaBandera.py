def dibujar_bandera (n):
    """ int --> nada
        OBJ: Dibuja una bandera doble con asteriscos de un ancho tamaño n """
    for k in range(2):
        for i in range(1,n+1):
            print (i*'* ')
        for j in range(1,n):
            print ((n-j)*'* ')