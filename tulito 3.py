valor= int(input('Ingrese un numero:'))
contador=0

if (valor<=0):
    print('Error numero no es valido')
else:
    for x in range (1,valor+1):
        if(valor%x==0):
            contador=contador+1
    if contador==2 or contador==1:
        print('El numero es primo')
    else:
        print('El numero no es primo')