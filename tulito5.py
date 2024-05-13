cant=int(input('Ingrese cuantas edades, va a ingresar:'))
lista= []
pos= 0
while pos<cant:
        
        valor= int(input('Ingrese edad:'))
        if (valor>0):
              
            lista.append(valor)
            pos=pos+1
        else:
             print('Numero no es valido, intentelo de nuevo')
mayor=0
for i in lista:
    if (i>mayor):
         mayor=i
print('El valor mayor es:'+ str(mayor))
