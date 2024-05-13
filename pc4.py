print('David Gil')
numero = int(input('Ingrese un numero: '))

residuo= numero % 2
if numero < 0 :
    print('es negativo')
else:
    print('es positivo') 
    if numero==0 :
        print('numero neutro')
    else:
        if residuo == 0:
            print('el numero es par')
        else:
            print('numero es impar')
        
