def contarSobresalientes():
    sobresaliente = 0
    noSobresaliente = 0
    i = 0
    for i in range (4):
        n = float(input('Introduzca una nota de  0 a 10: '))
        if n >=9:
            sobresaliente += 1

        elif n <=10:
            noSobresaliente += 1
    print("La cantidad de notas sobresalientes: ", sobresaliente,
          "\nLa cantidad de notas suspensas: ", noSobresaliente)
contarSobresalientes()





