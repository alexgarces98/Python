def hallarTablaLogica(x, y):
    booleanos = [True, False]

    print('x\ty\tx or y')
    print('-'*20)
    for x in booleanos:
       for y in booleanos:
          print(x, y, x or y, sep = '\t')
    print()

    return hallarTablaLogica(x, y)
