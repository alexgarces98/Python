def es_perfecto(n):
    """int -> bool #El retorno es True o False
    OBJ: Determina si n es perfecto (igual a la suma de sus divisores
         propios positivos
    PRE: n > 0"""

    sumatorio = 0 #el sumatorio debe inicializarse antes del bucle
    for i in range (1, n):
        if n % i == 0:
            sumatorio += i
    return sumatorio == n