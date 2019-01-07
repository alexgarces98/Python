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


