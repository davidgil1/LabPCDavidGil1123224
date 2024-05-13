print('Ejercicio 1: operaciones aritmeticas')

numero1= int(input('Ingrese un numero'))
numero2= int(input('Inhgrese un segundo numero'))

suma= numero1+numero2
resta= numero1-numero2
multiplicacion=numero1*numero2
divisionreal= numero1 / numero2 
divisionentera= numero1 // numero2 
mod= numero1 % numero2

print(numero1, '+', numero2, '=' , suma)
print(f'{numero1} + {numero2} = {suma}')

print(numero1, '-', numero2, '=' , resta)
print(f'{numero1} - {numero2} = {resta}')

print(numero1, '*', numero2, '=' , multiplicacion)
print(f'{numero1} * {numero2} = {multiplicacion}')

print(numero1, '/', numero2, '=' , divisionreal)
print(f'{numero1} / {numero2} = {divisionreal}')

print(numero1, '//', numero2, '=' , divisionentera)
print(f'{numero1} // {numero2} = {divisionentera}')

print(numero1, '%', numero2, '=' , mod)
print(f'{numero1} % {numero2} = {mod}')

print('Ejercicio 2: operaciones booleanas')

igualdad= numero1== numero2
diferentes= numero1 != numero2 
mayor= numero1 > numero2  
menor= numero1 < numero2 

print(numero1, '==', numero2, '=' , igualdad)
print(f'{numero1} == {numero2} = {igualdad}')

print(numero1, '!=', numero2, '=' , diferentes)
print(f'{numero1} != {numero2} = {diferentes}')

print(numero1, '>', numero2, '=' , mayor)
print(f'{numero1} > {numero2} = {mayor}')

print(numero1, '<', numero2, '=' , menor)
print(f'{numero1} < {numero2} = {menor}')

print('Ejercicio 3: jerarquia de operadores')

a= int(input('Ingrese el valor de a'))
b= int(input('Ingrese valor b'))
c= int(input('Ingrese valor c'))

operacion1= a*b+c
operacion2= a*b+c
operacion3= a/b+c
operacion4= 3*a+2*b/c**2 

print(f'operacio1={operacion1}')
print(f'operacion2={operacion2}')
print(f'operacion3={operacion3}')
print(f'operacion4={operacion4}')

print('Actividad 3')
print('Ejercicio 1: conversiones')

metros1= int(input( 'Ingrese metros: '))
km= metros1 / 1000
millas= metros1/ 16900
pies= metros1* 3.28
pulgadas= metros1 * 3.28 * 12

print(f'km={km}')
print(f'millas={millas}')
print(f'pies={pies}')
print(f'pulgadas={pulgadas}')

print('Ejercicio 2: ')

metros2= int(input( 'Ingrese otra cantidad de metros: '))
yardas= metros2 // 0.9144
modyardas= metros2 % 0.9144
pies= modyardas // 0.333333
print(f'yardas={yardas}')
print(f'pies={pies}')