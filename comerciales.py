'''Una empresa almacena los datos de sus comerciales en una estructura de datos que contiene los siguientes campos:
    nombre, apellidos, provincia que tiene asignada y ventas realizadas para el mes. Las ventas del mes es un array para
    cada comercial, donde se almacenan día por día las ventas de esa persona. Como se asume que todos los comerciales
    trabajan el mismo número de días en cada mes, para calcular su sueldo se emplea un sueldo base que es fijo e igual para
    todos, más una parte variable que depende de las ventas mensuales de cada uno. Realizar una función en Python que reciba
    la estructura de datos con la información de los comerciales y el importe del sueldo base y la ordene ascendentemente
    por sueldo bruto.
'''

class Comercial:

    def __init__(self, nom, ape, prov, vent):
        self.nombre = nom
        self.apellidos = ape
        self.provincia = prov
        self.ventas = vent

def es_menor(comercial1, comercial2):
    ventas_comercial1 = 0
    ventas_comercial2 = 0
    for i in range(len(comercial1.ventas)):
        ventas_comercial1 += comercial1.ventas[i]
        ventas_comercial2 += comercial2.ventas[i]
    return (ventas_comercial1 < ventas_comercial2)

def ascender(v, inicio, fin):
    for i in range(fin, inicio, -1):
        if es_menor(v[i], v[i - 1]):
            temp = v[i]
            v[i] = v[i - 1]
            v[i - 1] = temp

def burbuja(v, inicio, fin):
    for pasada in range(inicio, fin):
        ascender(v, pasada, fin)

def ordenar(lista, sueldo_base):
    """ list, float -> list
        OBJ: Ordena la lista de empleados por ventas
    """

    burbuja(lista_ventas, 0, len(lista) - 1)
    return lista

def mostrar(lista):
    """ list -> None
        OBJ: Muestra la lista de empleados en pantalla
    """
    print('Lista de empleados ordenados por sueldo bruto: ')
    for i in lista:
        print(i.nombre)

#Programa de prueba
lista_ventas = []
comercial = Comercial('Angel', 'Blecua', 'Guadalajara', [2300, 1000, 4000, 1030, 2200])
lista_ventas.append(comercial)
comercial = Comercial('Andrea', 'Jimenez', 'Cuenca', [3000, 1500, 1800, 1000, 4200])
lista_ventas.append(comercial)
comercial = Comercial('Luis', 'Blazquez', 'Avila', [2000, 9000, 4800, 7030, 6200])
lista_ventas.append(comercial)
sueldo_base = 2000
ordenar(lista_ventas, sueldo_base)
mostrar(lista_ventas)