'''Una aplicación móvil permite gestionar los cumpleaños de tus contactos. Para ello almacena de cada uno su fecha de
nacimiento, nombre y número de teléfono. Para completar la aplicación, se pide:

- Un subprograma que retorne una lista con los teléfonos y nombres de los contactos que cumplen años en un cierto mes.'''

def cumplen_este_mes(lista_contactos, mes):
    """ lista, int -> lista
        OBJ: Retorna una lista con los teléfonos y nombres de los contactos que cumplen años en un cierto mes.
        PRE: Existe el registro "Contacto" con fecha de nacimiento
    """
    cumpleanyeros = []
    for contacto in lista_contactos:
        if contacto.fecha_nac.mes == mes:
                cumpleanyeros.append([contacto.nombre, contacto.telefono])
    return cumpleanyeros

'''
    - Una función que retorna el mes en que hay más cumpleaños.
'''

def mes_mas_cumplen(lista_contactos):
    """ lista -> int
        OBJ: A partir de una lista de los contactos retorna el número del mes en que más contactos cumplen años.
        PRE: Existe un tipo registro "Contacto" con fecha de nacimiento
    """
    meses = [0 for i in range (12)]
    for contacto in lista_contactos:
        meses[contacto.fecha_nac.mes] += 1
    return meses.index(max(meses))

'''
    - Una función que permita añadir un contacto nuevo a una lista de contactos ya creada. Será una inserción ordenada pues
 el array de contactos se mantiene en memoria ordenado alfabéticamente por nombre
'''

def insertar_ordenado (lista_contactos,contacto):
    lista_contactos.append(contacto)
    i = len(lista_contactos)-1
    while (lista_contactos[i-1].nombre > contacto.nombre and i>0):
        lista_contactos[i] = lista_contactos[i-1]
        i -= 1
    lista_contactos[i] = contacto

'''
    - Una función que permita reordenar el array de contactos en orden creciente por el día de cumpleaños.
'''

def es_menor(contacto1, contacto2):
    """ Contacto, Contacto -> bool
        OBJ: determina contacto1 < contacto 2 según el valor del campo Fecha de nacimiento
    """
    return (contacto1.fecha_nac.mes < contacto2.fecha_nac.mes) or \
        ((contacto1.fecha_nac.mes == contacto2.fecha_nac.mes) and \
            (contacto1.fecha_nac.dia == contacto2.fecha_nac.dia))