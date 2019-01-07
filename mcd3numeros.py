def maximo_comun_divisor(x, y, z):
    """int, int, int -> int
    OBJ: maximo común divisor de x, y, z
    """
    div = 0
    top = min(abs(x), abs(y), abs(z))
    for i in range(1, top + 1):
        if x % i == 0 and y % i == 0 and z % i == 0:
            div = i
    return div

print(maximo_comun_divisor(25, -25, 25*5), '25')
print(maximo_comun_divisor(5, -25, 5), '5')

