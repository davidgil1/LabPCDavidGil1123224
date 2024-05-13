datos=int(input('Ingrese cuantos datos quiere ingresar:'))
edad= int(input('Ingrese el limite de edad que quiere: '))
cuantos=0
lista=[]

for x in range (datos):

    i= int(input('Ingrese edad:'))
    lista.append(i)

for i in lista:
    if i>=edad:
        cuantos+=1

        print('Hay', cuantos)
