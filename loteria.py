'''Un boleto de la Lotería Primitiva está formado por 8 apuestas, cada una de las cuales incluye 6 números entre el 1
y el49. Programe un módulo recursivo que determine el mayor número de aciertos de un boleto de apuestas. Se considera
premiada toda apuesta donde haya 4 o más aciertos.

El módulo recursivo deberá recibir al menos una lista de 6 números (resultado del sorteo) y un boleto de la Loteria
Primitiva, todo ello ordenado ascendentemente.

En el ejemplo mostrado en la figura, si la combinación ganadora hubiera sido 8-11- 13-16-34-43, su módulo habría
determinado que se trata de un boleto ganador de 5 aciertos, pues como se ve, la tercera apuesta incluye 5 de los
números de la combinación ganadora '''

def aciertos(apuesta,combinacion_ganadora):
    aciertos = 0
    for numero in apuesta:
        if numero in combinacion_ganadora:
            aciertos += 1
    return aciertos


def maximo_premio (lista_apuestas,combinacion_ganadora):
    """ lista, lista -> bool
        OBJ: Determina el máximo número de aciertos de una apuesta de la lotería primitiva.
        PRE: apuestas y comb. ganadora ordenados ascendentemente
    """
    if lista_apuestas == []:
        resultado = 0
    else:
        aciertos_actual=aciertos(lista_apuestas[0],combinacion_ganadora)
        if aciertos_actual == 6:
            resultado = 6
        else:
            resultado = max(aciertos_actual, \
                            maximo_premio(lista_apuestas[1:],combinacion_ganadora))
    return resultado