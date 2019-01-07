def meses_intermedios(d1,m1,d2,m2):
    """ int,int,int,int --> int
    OBJ: Número de meses completos entre dos fechas
    PRE: 1 < d1 | d2 < 30, 1 < m1|m2 < 12 """
    if not ((1 <= d1 <= 30) and
            (1 <= d2 <= 30) and
            (1 <= m1 <= 12) and
            (1 <= m2 <= 12)):
        return -1
    else:
        if m1 > m2 or (m1==m2 and d1>d2):
            m1,m2 = m2,m1
            d1,d2 = d2,d1
        elif m1 == m2: return 0
        num_meses = m2 - m1 - 1
        if d1 <15 and d2 > 15:
            num_meses += 1
        return num_meses
# Programa de prueba
print(meses_intermedios(2,1,15,4))
print(meses_intermedios(10,1,18,4))