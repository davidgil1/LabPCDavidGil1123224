
print('Hechor por David Gil')

#Actividad 1

print('Semana No. 10: Ejercicio 1')

mesEntrada = int(input('Ingrese un numero del 1-12:'))
mesSalida = ''

match mesEntrada:
    case 1 : 
        mesSalida= 'Enero'
    case 2 : 
        mesSalida='Febrero'
    case 3 : 
        mesSalida= 'Marzo'
    case 4 : 
        mesSalida='Abril'
    case 5 : 
        mesSalida= 'Mayo'
    case 6 : 
        mesSalida='Junio'
    case 7 : 
        mesSalida= 'Julio'
    case 8 : 
        mesSalida='Agosto'
    case 9 : 
        mesSalida= 'Septiembre'
    case 10 : 
        mesSalida='Octubre'
    case 11 : 
        mesSalida= 'Noviembre'
    case 12 : 
        mesSalida='Diciembre'
    case _:
        print('Error: El numero a ingresar debe de estar entre el 1 al 12')

print(f'Mes: {mesSalida} ')

#Actividad 2

print('Semana No. 10: Ejercicio 2')

a= int(input('Ingrese el primer numero a 0: '))
b= int(input('Ingrese el segundo numero a 0: '))
c= int(input('Ingrese el tercer numero a 0: '))

if( a<= 0 or b<=0 or c<=0 ):
    print('Error : Ingrese numero mayor que 0')

if(a>b):
    if(a>c):
        print ('El primer numero es el numero mayor:')
    else:
        if(a==c):
            print('El primer numero es mayor que el segundo pero igual que el tercero:')
        else:
            print('El primer numero es mayor que el segundo y menor que el tercero:')
else:
    if(a==b):
        if(a>c):
            print('El primer numero es igual que el segundo numero pero mayo que el tercero:')
        else:
            if (a==c):
                print('El primer numero es igual que el segundo y tercero:')
            else: 
                print('El primer numero es igual que el segundo pero menor que el tercero:')
        if (b>c):
            print('El segundo numero es igual que el primer numero pero mayor que el tercero:')
        else:
            if (b==c):
                print('El segundo numero es igual que el primer numero y tercero:')
            else:
                print('El segundo numero es igual que el primer dia pero menor que el tercero:')

        
#Actividad 3

print('Semana No. 10: Ejercicio 3 ')

dia= int(input('Ingrese el dia que nacio:'))
mes= int(input('Ingrese el numero de mes en que nacio:'))
ano= int(input('Ingrese el año que nacio:'))

if (dia<32 or mes<13):
    if mes== 1:
        if 1<=dia<=19:
            print('Eres Capricornio: ')
        else: 
            print('Erers Acuario: ')
    else: 
        if mes== 2:
            if 1<=dia<=18:
                print('Eres  Acuario: ')
            else: 
                print('Eres Piscis: ')
        else:
            if mes== 3:
                if 1<=dia<=20:
                    print('Eres  Piscis: ')
                else: 
                    print('Eres Aries: ')      
                    if mes==4:
                        if 1<=dia<=19:
                            print('Eres Aries:')
                        else:
                            print('Eres Tauro: ')
                    else:
                        if mes==5:
                            if 1<=dia<=20:
                                print('Eres Tauro: ')
                            else:
                                print('Eres Geminis: ')
                        else:
                            if mes==6:
                                if 1<=dia<=20:
                                    print('Eres Geminins: ')
                                else:
                                    print('Eres Cancer: ')
                            else:
                                if mes==7: 
                                    if 1<=dia<=22:
                                        print('Eres Cancer: ')
                                    else: 
                                        print('Eres Leo: ')
                                else:
                                    if mes==8:
                                        if 1<=dia<=22:
                                            print('Eres Leo')
                                        else: 
                                            print('Eres Virgo: ')
                                    else:
                                        if mes==9:
                                            if 1<=dia<=22:
                                                print('Eres Virgo: ')
                                            else:
                                                print('Eres Libra: ')
                                        else:
                                            if mes==10:
                                                if 1<=dia<=22:
                                                    print('Eres Libra: ')
                                                else: 
                                                    print('Eres Escorpio: ')
                                            else:
                                                if mes==11:
                                                    if 1<=dia<=21:
                                                        print('Eres Escorpio: ')
                                                    else:
                                                        print('Eres Sagitario: ')
                                                else:
                                                    if mes==12:
                                                        if 1<=dia<=21:
                                                            print('Eres Sagitario: ')
                                                        else:
                                                            print('Eres Capricornio:')
                                                    else:
                                                        print('....')
else:
    print('No es valido esa cantidad')