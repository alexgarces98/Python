# Archivo:.py
# # Autor: Alejandro García
# # Fecha: 24/11/2018
# # Descripción: Implemente una aplicación para ayudar en la gestión de cobros de una gasolinera. Mediante 3 arrays deberá
# # calcular el gasto de un total de 10 clientes. El primer array será utilizado para almacenar el gasto de cada cliente
# # en gasolina, el segundo array será utilizado para almacenar el gasto en productos de la tienda de la gasolinera, el
# # tercer array almacenará la suma de los dos arrays anteriores. La aplicación:
# # a. Solicitará por teclado los gastos de gasolina y de la tienda para cada uno de los 10 clientes.
# # b. Mostrará por pantalla la suma de los gastos para cada cliente.

def pedir_gasto_gasolina():
    lista_gasto_gasolina = []
    print('GASTOS DE GASOLINA:')
    for i in range (10):
        print('********Cliente ',i+1,'********')
        gasto_gasolina = int(input('Introduce el gasto del cliente en gasolina: '))
        lista_gasto_gasolina.append(gasto_gasolina)
    return lista_gasto_gasolina


def pedir_gasto_tienda():
    lista_gasto_tienda = []
    print('GASTOS DE LA TIENDA:')
    for i in range(10):
        print('********Cliente ',i+1,'********')
        gasto_tienda = int(input('Introduce el gasto del cliente en la tienda: '))
        lista_gasto_tienda.append(gasto_tienda)
    return lista_gasto_tienda


def gasto_total(lista_gasto_gasolina,lista_gasto_tienda):
    lista_gasto_total = []
    for i in range (10):
        lista_gasto_total.append(lista_gasto_gasolina[i]+lista_gasto_tienda[i])
    return lista_gasto_total

def imprimir_lista_gastos():
    print('-------------------')
    print('Lista de gastos de gasolina: ',lista_gasto_gasolina)
    print('Lista de gastos de la tienda: ',lista_gasto_tienda)
    print('Lista de gastos totales: ',lista_gasto_total)
    print('-------------------')

def imprimir_gastos():
    for i in range (10):
        print('Los gastos del cliente',i+1,'son:')
        print('Gastos en gasolina: ',lista_gasto_gasolina[i])
        print('Gastos en la tienda: ',lista_gasto_tienda[i])
        print('Gastos total: ',lista_gasto_total[i])
        print('------------------')


lista_gasto_gasolina = pedir_gasto_gasolina()
lista_gasto_tienda = pedir_gasto_tienda()
lista_gasto_total = gasto_total(lista_gasto_gasolina,lista_gasto_tienda)
imprimir_lista_gastos()
imprimir_gastos()


