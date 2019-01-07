class Jugador:
    def __init__(self, nom, gol, pos, equip):
        self.nombre = nom
        self.goles = gol
        self.posicion = pos
        self.equipo = equip
lista_federacion = []
# ejemplo de introducción de jugador
jugador = Jugador('Messi',25,'delantero','FCBarcelona')
lista_federacion.append(jugador)
jugador = Jugador('Suarez',30,'delantero','FCBarcelona')
lista_federacion.append(jugador)
jugador = Jugador('Ronaldo',28,'delantero','RMadrid')
lista_federacion.append(jugador)
jugador = Jugador('Benzema',21,'delantero','RMadrid')
lista_federacion.append(jugador)
jugador = Jugador('Bale',22,'delantero','RMadrid')
lista_federacion.append(jugador)
jugador = Jugador('Giezmann',26,'delantero','ATMadrid')
lista_federacion.append(jugador)

def candidatos(lista_jugadores, inicio, fin):
    """ list, int, int -> int
        OBJ: Computa el número de candidatos a mejor delantero
    """
    if inicio > fin:
        resultado = 0
    else:
        if (lista_jugadores[inicio].posicion == "delantero" and
                lista_jugadores[inicio].goles >= 20):
            resultado = 1 + candidatos(lista_jugadores, inicio+1, fin)
        else:
            resultado = candidatos(lista_jugadores, inicio+1, fin)
    return resultado
print(candidatos(lista_federacion,0,len(lista_federacion)-1))

def es_candidato_a_premio(jugador):
    """ jugador --> bool
        OBJ: Si un jugador es delantero y marca más de 20 goles es candidato
    """
    return jugador.goles > 20 and jugador.posicion=='delantero'


def obtener_equipos_con_candidatos(lista):
    """ list -> dictionary
        OBJ: Genera un diccionario con todos los clubes de fútbol que tienen al menos un candidato en la competición
        al mejor delantero
    """
    clubes_premio = {}
    for jugador in lista:
        if es_candidato_a_premio(jugador):
            if jugador.equipo not in clubes_premio:
                clubes_premio[jugador.equipo] = 1
            else:
                clubes_premio[jugador.equipo] += 1
    return clubes_premio


def es_menor(equipo1, equipo2):
    """ list -> bool
        OBJ: Compara si son menores los elementos de la pos 1 de dos listas
    """
    return equipo1[1] < equipo2[1]


def ascender(v,inicio,fin):
    for i in range (fin,inicio,-1):
        if es_menor(v[i],v[i-1]):
            temp = v[i]
            v[i] = v[i-1]
            v[i-1] = temp


def burbuja (v,inicio,fin):
    for pasada in range (inicio,fin) :
        ascender(v,pasada,fin)



def mostrar_candidatos_ordenados(lista_federacion):
    """ list -> None
        OBJ: Muestra por pantalla todos los clubes de fútbol que tienen al menos un candidato en la competición al mejor
         delantero, ordenados descendentemente de más a menos candidatos
    """
    candidatos = obtener_equipos_con_candidatos(lista_federacion)
    # transformamos el diccionario en una lista, para ordenar los datos
    lista_candidatos = []
    for equipo in candidatos:
        lista_candidatos.append([equipo,candidatos[equipo]])
    # Aplicamos el método de ordenación burbuja a la lista, usando como # criterio de ordenación el número de candidatos
    #  por equipo burbuja(lista_candidatos,0,len(lista_candidatos)-1)
    lista_candidatos.reverse()
    for equipo in lista_candidatos:
        print(equipo[0],'-',equipo[1],'candidatos')
# Programa de prueba
lista_federacion = []
jugador = Jugador('Messi',25,'delantero','FCBarcelona')
lista_federacion.append(jugador)
jugador = Jugador('Suarez',30,'delantero','FCBarcelona')
lista_federacion.append(jugador)
jugador = Jugador('Ronaldo',28,'delantero','RMadrid')
lista_federacion.append(jugador)
jugador = Jugador('Benzema',21,'delantero','RMadrid')
lista_federacion.append(jugador)
jugador = Jugador('Bale',22,'delantero','RMadrid')
lista_federacion.append(jugador)
jugador = Jugador('Giezmann',26,'delantero','ATMadrid')
lista_federacion.append(jugador)
mostrar_candidatos_ordenados(lista_federacion)