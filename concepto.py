n=int(input("Ingrese la cantidad de numeros que desea ingresar:"))
lista=[]
for i in range (n):

    valor= int(input('Ingrese un numero:'))
    lista.append(valor)

sumatoria=0
for i in lista:
    sumatoria= sumatoria+i
    promedio= sumatoria/n

    print('El promedio es',str(promedio))
numerador=0
for i in lista:
    numerador= (promedio)
