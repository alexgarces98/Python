'''Programe una función recursiva en Python que calcule el número de “triunfos” de que hay en una baraja española de 40
cartas (array de cartas) entre dos posiciones. Las cartas son registros con palo (oros, copas, espadas o bastos) y valor
 (números enteros del 1 al 7 y del 10 al 12), y se consideran “triunfos” el as, el 3, la sota (10), el caballo (11) y el
  rey (12).'''


def suma_triunfos(baraja, inicio, fin):
    
    """ lista, int, int, string -> int
        OBJ: Determina el número de cartas "triunfo" (as,3,10,11 y 12) entre 2 límites [inicio..fin] en una baraja de cartas
        PRE: Existe un tipo registro "Carta" con dos campos: palo y valor
    """

    if inicio > fin:
        resultado = 0
    else:
        if baraja[0].valor in [1,3,10,11,12]:
            resultado = 1 + suma_triunfos(baraja, inicio+1, fin)
        else:
            resultado = suma_triunfos(baraja, inicio+1, fin)
    return resultado