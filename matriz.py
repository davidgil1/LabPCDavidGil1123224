#matriz=[[1,2,3],[4,5,6],[7,8,9]]
#for fila in matriz:
    #for valor in fila:
        #print(str(valor),end=' ')
    #print()

def crear_matriz(filas,columnas):
    matriz= []
    for i in range(filas):
        fila=[]
        for j in range (columnas):
            valor=int(input(f'Ingrese el valor para[{i},{j}]: '))
            fila.append(valor)
            matriz.append(fila)
        return matriz
    
f = int(input('Ingrese valor para las filas:'))
c= int(input('ingrese valor para columnas'))
matriz= crear_matriz(f,c)
for fila in matriz:
    print(fila)

