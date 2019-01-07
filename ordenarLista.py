def es_menor(lista1, lista2):
    """ lista, lista -> bool
        OBJ: determina lista1<lista2 según el valor absoluto de sus elementos
    """
    menor1 = abs(lista1[0])
    menor2 = abs(lista2[0])
    for elem in lista1[1:]:
        actual = abs(elem)
        if actual < menor1: menor1 = actual
    for elem in lista2[1:]:
        actual = abs(elem)
        if actual < menor2: menor2 = actual
    return menor1 < menor2

