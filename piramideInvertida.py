i = r =3
while i>0:
  for s in range(r-i):
     print("  ",end='') # Dos espacios
  for j in range(i, 2*i):
     print(j, end=' ')
  for k in range(j, j+i-1):
       print(k, end=' ')
  print("\n")
  i -= 1