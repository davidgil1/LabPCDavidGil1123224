n=int(input("Ingrese un numreo positivo mayor a 0: "))
n2= int(input('Ingrese un segundo numero mayor a 0:'))

if n<0 or n2<0:
    print("EL numero debe ser mayor a 0")

else:
    suma=0

    for x in range (1,n):
        if n%x == 0:
            suma +=x
    if suma==n:
        print("El numero es perfecto")
    else:
        print("El numero no es perfecto")
    suma2=0
    for x in range (1,n2):
        if n2%x == 0:
            suma2 +=x
    if suma2==n2:
        print("El numero es perfecto")
    else:
        print("El numero no es perfecto")
if suma2==suma:
    print('Los numeros son amigos')
else:
    print('Los numeros no son amigos')
