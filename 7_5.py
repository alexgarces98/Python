# Archivo:5.py
# # Autor: Alejandro García
# # Fecha: 08/12/2018
# # Descripción: Haga un programa para gestionar las notas de una clase de 20 alumnos de los cuales sabemos el nombre y
# la nota. El programa debe permitir:
# a. Introducir los datos de los alumnos por teclado.
# b. Dado un nombre de un alumno, buscarlo y modificar su nota, mostrando el resultado por pantalla
# (empleando búsqueda secuencial).
# c. Dado un nombre de un alumno, buscarlo y mostrar la información por pantalla empleando búsqueda binaria.
# d. Realizar la media de todas las notas.
# e. Realizar la media de las notas superiores a 5.
# f. Realizar la ordenación (método de selección) de los alumnos por notas en orden descendente y mostrar la nota del
# alumno con mejor nota.
# g. Utilizando el método de inserción, realizar la ordenación de los alumnos por notas en orden ascendente y mostrar la
# nota del alumno que peor nota haya sacado.


class rAlumno:
    def __init__ (self, n,nota):
        self.nombre=n
        self.nota=nota

def introducirAlumnos(lAlumnos):
    for i in range(3):
        n=input('Nombre alumno:')
        nota=float(input('Nota alumno: '))
        a=rAlumno(n,nota)
        lAlumnos.append(a)
    return lAlumnos

def buscarAlumnos(l, n):
    enc = False
    i = 0
    while not enc and i<len(l):
        if l[i].nombre==n:
            enc = True
        else:
            i += 1
    if enc:
        resultado = i

    else:
        resultado = -1

    return resultado

def modificarNota(lAlumnos, nombreAlumno, notaNueva):
    pos = buscarAlumnos(lAlumnos, nombreAlumno)
    if pos != -1:
        lAlumnos[pos].nota = notaNueva
    return lAlumnos


def ordenarAlumnosNombre(lAlumnos):
    ini = 0
    fin = len(lAlumnos) - 1

    for pasada in range(ini, fin):
        for i in range(ini, fin):
            if lAlumnos[i].nombre > lAlumnos[i + 1].nombre:
                temp = lAlumnos[i]
                lAlumnos[i] = lAlumnos[i + 1]
                lAlumnos[i + 1] = temp

    return lAlumnos


def buscarPorNombreBinario(lAlumnos, nombre):
    lAlumnos = ordenarAlumnosNombre(lAlumnos)
    enc = False
    ini = 0
    fin = len(lAlumnos) - 1
    pos = -1

    while not enc and ini <= fin:

        centro = (ini + fin) // 2

        if lAlumnos[ini].nombre == nombre:
            pos = centro
            enc = True

        elif nombre < lAlumnos[centro].nombre:

            fin = centro - 1

        else:

            ini = centro + 1

    return pos

def sumarNotas(lAlumnos):
    if len(lAlumnos) == 1:

        sumaNotas = lAlumnos[0].nota

    else:

        sumaNotas = lAlumnos[0].nota + sumarNotas(lAlumnos[+1:])

    return sumaNotas


def calcularMedia(lAlumnos):
    return sumarNotas(lAlumnos) / len(lAlumnos)


def sumarNotasMayores(lAlumnos):
    if len(lAlumnos) == 1:

        if lAlumnos[0].nota < 5:
            sumaNotas = 0
        else:
            sumaNotas = lAlumnos[0].nota
    else:
        if lAlumnos[0].nota < 5:
            sumaNotas = sumarNotasMayores(lAlumnos[+1:])

        else:
            sumaNotas = lAlumnos[0].nota + sumarNotasMayores(lAlumnos[+1:])

    return sumaNotas


def numeroNotasMayores(lAlumnos):
    contador = 0

    for lAlumnos in lAlumnos:
        if lAlumnos.nota >= 5:
            contador += 1

    return contador


def calcularMediaMayores(lAlumnos):
    return sumarNotasMayores(lAlumnos) / numeroNotasMayores(lAlumnos)

def ordenarNotasSeleccion(lAlumnos, ini, fin):
    for pasada in range(ini, fin):

        mayor = pasada

        for i in range(pasada + 1, fin + 1):

            if lAlumnos[i].nota > lAlumnos[mayor].nota:
                mayor = i

        temp = lAlumnos[pasada]

        lAlumnos[pasada] = lAlumnos[mayor]

        lAlumnos[mayor] = temp

    return lAlumnos, lAlumnos[0]

def ascendenteInsercion(lAlumnos):
    for i in range(len(lAlumnos)):
        for j in range(i,0,-1):
            if(lAlumnos[j-1].nota > lAlumnos[j].nota):
                aux=lAlumnos[j]
                lAlumnos[j]=lAlumnos[j-1]
                lAlumnos[j-1]=aux

lAlumnos=[]
lAlumnos=introducirAlumnos(lAlumnos)
nombre=input('¿Nombre alumno?')
notaNueva=float(input('Nueva nota: '))
lAlumnos= modificarNota(lAlumnos, nombre, notaNueva)


print(ordenarNotasSeleccion())
print ("El alumno con MEJOR nota ha sido", lAlumnos[0].nombre , lAlumnos[0].nota)

print(ascendenteInsercion(lAlumnos))
print ("El alumno con PEOR nota ha sido", lAlumnos[0].nombre , lAlumnos[0].nota)





