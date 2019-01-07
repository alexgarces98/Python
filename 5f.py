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

'''


def busquedaBinaria(lAlumno, nombre):

    primero = 0
    ultimo = len(lAlumno)-1
    enc = False
    while primero <= ultimo and not enc:
        pm = (primero + ultimo)//2
        if nombre == lAlumno[pm].nombre:
            enc = True
        else:
            if nombre < lAlumno[pm].nombre:
                primero = pm-1
            else:
                if nombre > lAlumno.nombre:
                    ultimo = pm-1
    return enc




def mediaNotasSuperior5():

    return



def mediaNotas():
    suma = 0
    n_notas = 0
    i = 0
    while suma < len(lAlumnos):
        alumno = lAlumnos[i]
        nota = alumno.nota
        suma += nota
        n_notas += 1
    media = n_notas / len(lAlumnos)
    return media

'''

def ordenamientoSeleccion(lAlumnos):
   for intercambio_posicion in range(len(lAlumnos)-1,0,-1):
       elemento_mayor = 0
       for posicion in range(1,intercambio_posicion+1):
           if lAlumnos[posicion]<lAlumnos[elemento_mayor]:
               elemento_mayor = posicion

       temp = lAlumnos[intercambio_posicion]
       lAlumnos[intercambio_posicion] = lAlumnos[elemento_mayor]
       lAlumnos[elemento_mayor] = temp

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

print = lAlumnos


print(ordenamientoSeleccion(lAlumnos))
print ("El alumno con MEJOR nota ha sido", lAlumnos[0].nombre , lAlumnos[0].nota)

print(ascendenteInsercion(lAlumnos))
print ("El alumno con PEOR nota ha sido", lAlumnos[0].nombre , lAlumnos[0].nota)


