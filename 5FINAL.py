# Ejercicio 5

### REGISTROS ###

class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


### SUBPROGRAMAS ###

def introducirNotas(alumnos):
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))

    nuevo_alumno = Alumno(nombre, nota)
    alumnos.append(nuevo_alumno)

    return alumnos


def buscarNombreSecuencial(nombre, alumnos):
    pos = -1
    enc = False
    ini = 0

    while not enc and ini < len(alumnos):

        if alumnos[ini].nombre == nombre:
            pos = ini
            enc = True

        else:
            ini += 1

    return pos


def modificarNota(nombre, nota, alumnos):
    alumnos[buscarNombreSecuencial('maria', alumnos)].nota = nota

    return alumnos


def ordenarAlumnosNombre(alumnos):
    ini = 0
    fin = len(alumnos) - 1

    for pasada in range(ini, fin):
        for i in range(ini, fin):
            if alumnos[i].nombre > alumnos[i + 1].nombre:
                temp = alumnos[i]
                alumnos[i] = alumnos[i + 1]
                alumnos[i + 1] = temp

    return alumnos


def buscarPorNombreBinario(alumnos, nombre):
    alumnos = ordenarAlumnosNombre(alumnos)
    enc = False
    ini = 0
    fin = len(alumnos) - 1
    pos = -1

    while not enc and ini <= fin:

        centro = (ini + fin) // 2

        if alumnos[ini].nombre == nombre:
            pos = centro
            enc = True

        elif nombre < alumnos[centro].nombre:

            fin = centro - 1

        else:

            ini = centro + 1

    return pos


# con recursividad...¡OLÉ! ¡OLÉ!
def sumarNotas(alumnos):
    if len(alumnos) == 1:

        sumaNotas = alumnos[0].nota

    else:

        sumaNotas = alumnos[0].nota + sumarNotas(alumnos[+1:])

    return sumaNotas


def calcularMedia(alumnos):
    return sumarNotas(alumnos) / len(alumnos)


def sumarNotasMayores(alumnos):
    if len(alumnos) == 1:

        if alumnos[0].nota < 5:
            sumaNotas = 0
        else:
            sumaNotas = alumnos[0].nota
    else:
        if alumnos[0].nota < 5:
            sumaNotas = sumarNotasMayores(alumnos[+1:])

        else:
            sumaNotas = alumnos[0].nota + sumarNotasMayores(alumnos[+1:])

    return sumaNotas


def numeroNotasMayores(alumnos):
    contador = 0

    for alumno in alumnos:
        if alumno.nota >= 5:
            contador += 1

    return contador


def calcularMediaMayores(alumnos):
    return sumarNotasMayores(alumnos) / numeroNotasMayores(alumnos)


def ordenarNotasSeleccion(alumnos, ini, fin):
    for pasada in range(ini, fin):

        mayor = pasada

        for i in range(pasada + 1, fin + 1):

            if alumnos[i].nota > alumnos[mayor].nota:
                mayor = i

        temp = alumnos[pasada]

        alumnos[pasada] = alumnos[mayor]

        alumnos[mayor] = temp

    return alumnos, alumnos[0]


### PROGRAMA ###

a1 = Alumno("pepe", 7)
a2 = Alumno("paco", 4.7)
a3 = Alumno("sandra", 9.75)
a4 = Alumno("maria", 5)
a5 = Alumno("juan", 6.5)

alumnos = [a1, a2, a3, a4, a5]

# a)Introducir notas
#
# alumnos = introducirNotas(alumnos)
#

# b)Buscar y modificar nota alumno por nombre (secuencial)
alumnos = modificarNota('maria', 7.1, alumnos)

# c)Buscar y mostar datos alumno por nombre (binaria)
alumno_buscado = alumnos[buscarPorNombreBinario(alumnos, 'maria')]

print("Nombre:", alumno_buscado.nombre, "- Nota:", alumno_buscado.nota)

# d)Realizar media de las notas
media = calcularMedia(alumnos)

# e) Realizar media si la nota es más alta de 5
mediaMayor = calcularMediaMayores(alumnos)

# f) Ordenar las notas de los alumnos por seleccion y sacar la mayor nota
alumnos, alumnosMasNota = ordenarNotasSeleccion(alumnos, 0, len(alumnos) - 1)

for alumno in alumnos:
    print(alumno.nota)

print("Alumno con más nota:", alumnosMasNota.nombre, " - Nota:", alumnosMasNota.nota)


def ordenarSeleccion(lista, ini, fin):
    for pasada in range(ini, fin):

        menor = pasada

        for i in range(pasada + 1, fin + 1):
            if lista[i] < lista[menor]:
                menor = i

        temp = lista[pasada]

        lista[pasada] = lista[menor]

        lista[menor] = temp

    return lista


def buscarPorBinario(lista, ini, fin, elem):
    enc = False
    pos = -1

    while not enc and ini <= fin:

        centro = (ini + fin) // 2
        print("Centro:", centro)
        print("Elemento:", lista[elem])

        if lista[centro] == elem:

            enc = True
            pos = centro

        elif elem < lista[centro]:

            fin = centro - 1

        else:

            ini = centro + 1

    return pos


def ordenarPorBurbuja(lista, ini, fin):
    for pasada in range(ini, fin):
        for i in range(ini, fin):
            if lista[i] > lista[i + 1]:
                temp = lista[i]

                lista[i] = lista[i + 1]

                lista[i + 1] = temp

    return lista


lista = [0, 7, 1, 8, 19, 3, 5, 9, 0]

lista = ordenarSeleccion(lista, 0, len(lista) - 1)
lista2 = ordenarPorBurbuja(lista, 0, len(lista) - 1)

pos = buscarPorBinario(lista, 0, len(lista)-1, 0)
