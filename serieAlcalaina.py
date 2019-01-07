# 1, 2, 3, 8, 19, 86, 455...

def termino_serie(n):
    n_3 = 1
    n_2 = 2
    n_1 = 3
    i = 4
    while i<=n:
        t = n_3 + n_2*n_2 + n_1
        n_3 = n_2
        n_2 = n_1
        n_1 = t
        i += 1
    return t

print(termino_serie(6))
