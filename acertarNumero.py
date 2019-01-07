n = int(input("Introduce el número adivinar: "))
num = int(input("Pide a alguien que trate de adivinarlo. Apuesta: "))
a= 0
while(num!=n):
   a += 1
   if(num<n):
      print("Casi! El que me has dado es más pequeño que el que buscas")
   else:
      print("Casi! El que me has dado es más grande que el que buscas")
   num = int(input("Prueba de nuevo introduciendo otro número: "))
print('Por fin acertaste! Te ha costado ', a, 'intentos')