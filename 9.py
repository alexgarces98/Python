# Archivo: 9.py
# Autor: Alejandro García
# Fecha: 30/11/2018
# Descripción: Programar un algoritmo recursivo que obtenga la suma de las edades de todos
# los elementos de una lista de alumnos. Un alumno está caracterizado por tres
# atributos (nombre, edad, titulacion).

def sumaEdades(edad):
   if len(edad) == 1:
        return edad[0]
   else:
        return edad[0] + sumaEdades(edad[1:])



print(sumaEdades ([3,4,5,6,7,8]))