#Metodo para agregar cuadros negros y blancos al tablero
def imprimirtableroinicial(tablero):
    for i in range(0,8):
        for j in range(0,8):
            if i % 2 == 0:
                if j % 2 == 0:
                    tablero[i][j] = "\033[47m  \033[0m"
                else:
                    tablero[i][j] = "\033[40m  \033[0m"
            else: 
                if j % 2 == 0:
                    tablero[i][j] = "\033[40m  \033[0m"
                else:
                    tablero[i][j] = "\033[47m  \033[0m"
    imprimirtablerio(tablero)

#Metodo para imprimir el tablero recorriendo cada fila y columna     
def imprimirtablerio(tablero):
     print("    a b c d e f g h ")
     for i in range(0,8):
        print(f"{i+1}  ",end="")
        for j in range(0,8):
                    print(f"{tablero[i][j]}", end="")
        print()   

#Metodo para evaluar la entrada de Si o No
def evaluarSN():
    seguir = True
    print("Por favor, ingresa 's' para sí o 'n' para no: ")
    while seguir:#Ciclo while para que siga por si hay errores
        respuesta = input().strip().lower()#Se eliminan los espacios ingresados y se toma como minuscula
        if respuesta == 's':
            return True
        elif respuesta == 'n':
             return False
        else:
            print("Entrada no válida. Inténtalo de nuevo.")

#Metodo para agregar piezas   
def agregarpiezas(tablero,pnegras,pblancas):
    seguir = True
    valp = True
    valc = True
    valco = True
    valfi = True
    lapieza = ""
    fila = 0
    columna = 0
    #Metodo while para seguir hasta que el usuario diga que no
    while seguir:
         valp = True
         #Se reduce los errores posibles a la hora de preguntar al usuario dandole un menu         
         print("Elija la pieza a agregar: ")
         print("1. Rey")
         print("2. Reina")           
         print("3. Alfil")
         print("4. Torre")
         print("5. Caballo")
         print("6. Peon")
         #Metodo while que se repetira hasta que elija una opcion correcta
         while valp:
              resp = input()
              if resp.isdigit():  #Se evalua si es digito
                    resp = int(resp) #Se convierte la respuesta a entero
                    if resp <= 0 or resp >6: #Se evalua si esta entre las posibles opciones
                        print("Por favor elija una de las opciones, intentelo de nuevo, Presione Enter para volver a intentar")
                        input()
                    else:
                        resp = resp - 1 #Se le resta 1 ya que los arreglo se trabajan desde la posicion 0
                        valp = False #Esta correcto, se sale del ciclo de la pieza
              else:
                    #Mensaje de error si no es un numero
                    print()
                    print("La respuesta debe ser número entero. Por favor, inténtalo de nuevo, Presione Enter")
                    input()
         valc = True
         #Se reduce los errores posibles a la hora de preguntar al usuario dandole un menu         
         print("Elija el color de la pieza")
         print("1. Blanco")
         print("2. Negro")
         #Metodo while que se repetira hasta que no haya errores
         while valc:
              resc = input()
              if resc.isdigit():#Evalua si es dijito
                   resc = int(resc) #Se convierte a entero
                   if resc <= 0 or resc >2: #Se evalua si esta entre las opciones dadas
                        print("Por favor elija una de las opciones, intentelo de nuevo, Presione Enter para volver a intentar")
                        input()
                   else: 
                        #Se evalua en que lista de color de piezas se buscara
                        if resc == 1:
                             lapieza = pblancas[resp] #Se le asiga valor a la pieza actual segun eleccion del usuario
                             valc = False#Sale del ciclo while del color
                        elif resc == 2:
                             lapieza = pnegras[resp]
                             valc = False#Sale del ciclo while del color
                        
              else:
                   #Mensaje de error si no es un numero
                   print()
                   print("La respuesta debe ser número entero. Por favor, inténtalo de nuevo, Presione Enter")
                   input()
                   print()
                   print()
                   print()
         valfi = True
         #While para seguir hasta que este correcto
         while valfi:
              print("Ingrese la fila donde se ingresara (1 - 8)")
              fila = input()
              if fila.isdigit():#Se evalua si es digito
                   fila = int(fila)#Se convierte a entero
                   if fila <= 0 or fila >8:#Se evalua si esta dentro de las opciones posibles
                        print("Por favor ingrese una columna valida (1 - 8), Presione Enter para volver a intentar")
                        input()
                   else: 
                        fila = fila - 1#Se le resta 1 ya que los arreglo se trabajan desde la posicion 0
                        valfi = False#Sale del ciclo while de la fila
              else: 
                   #Mensaje de error si no es un numero
                   print()
                   print("La respuesta debe ser número entero. Por favor, inténtalo de nuevo, Presione Enter")
                   input()
         valco = True
         #Ciclo while para seguir hasta que este correcto lo que el usuario ingresa
         while valco:
              #Se da un menu para minimizar los errores por el ingreso de datos del usuario
              print("Ingrese la columna donde se ingresara")
              print("1. A")
              print("2. B")
              print("3. C")
              print("4. D")
              print("5. E")
              print("6. F")
              print("7. G")
              print("8. H")
              columna = input()
              if columna.isdigit():#Se evalua si es dijito la entrada
                   columna = int(columna)#Se convierte en entero
                   if columna <= 0 or columna >8: #Evalua si esta dentro de las opciones correctas
                        print("Por favor elija una de las opciones, Presione Enter para volver a intentar")
                        input()
                   else: 
                        columna = columna - 1#Se le resta 1 ya que los arreglo se trabajan desde la posicion 0
                        valco = False #Se toma como correcto por ende se sale del ciclo while
              else: 
                   #Mensaje de error si no es un numero
                   print()
                   print("La respuesta debe ser número entero. Por favor, inténtalo de nuevo, Presione Enter")
                   input()
         #Se evalua si el tablero en la posicion ingresada esta vacio, es decir no tiene pieza
         if tablero[fila][columna] == "\033[47m  \033[0m" or tablero[fila][columna] == "\033[40m  \033[0m":
              tablero[fila][columna] = f"{lapieza} " #Se asigna la pieza a la posicion deseada en el tablero
              print("Pieza agregada con exito, Desea ingresar otra pieza?")
              valseguir = evaluarSN() #Se pregunta si quiere ingresar otra pieza o no
              if valseguir:
                   seguir = True#Sigue dentro del ciclo para pedir piezas
              else: 
                   seguir = False #Sale del ciclo de pedir piezas
                   return
         else: 
              #Mensaje de error si la casilla ya esta ocupada
              print("Ya existe una pieza en esa posicion, Desea volver a intentar?")
              valseguir = evaluarSN() #Se evalua si quiere volver a intentar despues del error
              if valseguir:
                   seguir = True #Se reinicia el ciclo de pedir la pieza
              else: 
                   seguir = False #Se sale del ciclo de pedir la pieza
                   return
    print()

#Metodo para agregar el caballo a evaluar jugadas
def agregarcaballo(tablero,pnegras,pblancas):
    #Se recibe como parametro las listas con las piezas negras y blancas en Unicode
    valc = True
    valco = True
    valfi = True
    lapieza = ""
    fila = 0
    columna = 0
    #Ciclo while para que siga hasta que este correcta la interaccion del usuario
    while True:
         valc = True
         #Se da un menu para minimizar errores
         print("Elija el color del caballo")
         print("1. Blanco")
         print("2. Negro")
         while valc:
              resc = input()
              if resc.isdigit():#Se evalua si es digito
                   resc = int(resc)#Se convierte a entero
                   if resc <= 0 or resc >2: #Se evalua si estad dentro de las opciones disponibles
                        print("Por favor elija una de las opciones, intentelo de nuevo, Presione Enter para volver a intentar")
                        input()
                   else: 
                        if resc == 1:
                             lapieza = pblancas[4]#Se asigna el caballo a la pieza segun el color seleccionado
                             valc = False
                        elif resc == 2:
                             lapieza = pnegras[4]
                             valc = False
                        
              else:
                   #Mensaje de error si no se ingresa un numero
                   print()
                   print("La respuesta debe ser número entero. Por favor, inténtalo de nuevo, Presione Enter")
                   input()
                   print()
                   print()
                   print()
         print()
         print()
         valfi = True
         #Ciclo while para seguir hasta que no existe un error
         while valfi:
              print("Ingrese la fila donde se ingresara (1 - 8)")
              fila = input()
              if fila.isdigit():#Se evalua si es un numero
                   fila = int(fila) #Se convierte a entero
                   if fila <= 0 or fila >8: #Se evalua si esta dentro de las posibles respuestas correctas
                        print("Por favor ingrese una columna valida (1 - 8), Presione Enter para volver a intentar")
                        input()
                   else: 
                        fila = fila - 1 #Se le resta uno ya que en matrices y arreglos el indice empieza en 0
                        valfi = False #Se toma como correcto y se sale del ciclo
              else: 
                   #Mensaje de error si no es un numero
                   print()
                   print("La respuesta debe ser número entero. Por favor, inténtalo de nuevo, Presione Enter")
                   input()
         valco = True
         #Ciclo while para repetir si hay errores
         while valco:
              #Se da un menu para minimizar errores del usuario
              print("Ingrese la columna donde se ingresara")
              print("1. A")
              print("2. B")
              print("3. C")
              print("4. D")
              print("5. E")
              print("6. F")
              print("7. G")
              print("8. H")
              columna = input()
              if columna.isdigit():#Se evalua si es digito
                   columna = int(columna)#Se convierte en entero
                   if columna <= 0 or columna >8:#Se evalua si esta dentro de las opciones dadas
                        print("Por favor elija una de las opciones, Presione Enter para volver a intentar")
                        input()
                   else: 
                        columna = columna - 1#Se le resta uno ya que en matrices y arreglos el indice empieza en 0
                        valco = False#Se toma como correcto por ende se sale del ciclo
              else:
                   #Mensaje de error si no es un numero
                   print()
                   print("La respuesta debe ser número entero. Por favor, inténtalo de nuevo, Presione Enter")
                   input()
         #Se evalua si la casilla deseada esta vacia          
         if tablero[fila][columna] == "\033[47m  \033[0m" or tablero[fila][columna] == "\033[40m  \033[0m":
              tablero[fila][columna] = f"{lapieza} " #Se le asigna el caballo a la casilla deseada
              print(f"Caballo ingresado con exito, Presione Enter para desplegar la lista de movimietos")
              input()
              imprimirtablerio(tablero)
              evaluarcaballo(tablero,fila,columna,pnegras,pblancas,lapieza)
              input()
              return
         else: 
              #Mensaje de error si la casilla ya esta ocupada
              print("Ya existe una pieza en esa posicion, presione enter para volver a intentar")
    print()

#Metodo para validar las casillas
def validarcasilla(fila,columa,vf):     
     #Se recibe una lista de booleanos "vf"
     #Se evalua si las filas y las columnas de cada posible movimiento del caballo existen dentro del tablero
     if fila + 1 <= 7 and columa -2 <= 7:
          vf[0] = True
     if fila + 2 <= 7 and columa -1 <= 7:
          vf[1] = True
     if fila + 2 <= 7 and columa +1 <= 7:
          vf[2] = True
     if fila + 1 <= 7 and columa +2 <= 7:
          vf[3] = True
     if fila -1 <= 7 and columa +2 <= 7:
          vf[4] = True
     if fila -2 <= 7 and columa +1 <= 7:
          vf[5] = True
     if fila -2 <= 7 and columa -1 <= 7:
          vf[6] = True
     if fila - 1 <= 7 and columa -2 <= 7:
          vf[7] = True
     return     

#Metodo para evaluar los movimientos del caballo
def evaluarcaballo(tablero,fila,columna,pnegras,pblancas,pieza):
    #Se define el arreglo usado para saber si la casilla existe dentro del tablero
    vf = [False,False,False,False,False,False,False,False]
    letras = ['a','b','c','d','e','f','g','h']
    misfilas = [1,2,3,4,5,6,7,8]
    #Filas finles de cada movimiento posible del caballo
    filas = [(fila +1),(fila+2),(fila+2),(fila+1),(fila-1),(fila-2),(fila-2),(fila-1)]
    #Columnas finales de cada movimiento posible del caballo
    columnas = [(columna-2),(columna-1),(columna+1),(columna+2),(columna+2),(columna+1),(columna-1),(columna-2)]
    #Se validan si las casillas de posible movimiento del caballo existen dentro del tablero
    validarcasilla(fila,columna,vf)
    #Se eliminan los espacios con la funcion .strip() por la forma que estan guardadas las piezas
    if pieza.strip() in pnegras: #Se evalua si el caballo es negro
        for i in range(0,8): #Ciclo for para analizar cada uno de los posibles 8 movimientos
             if vf[i] == True: #Si existe la casilla se evalua el movimiento
                  if tablero[filas[i]][columnas[i]] == "\033[47m  \033[0m" or tablero[filas[i]][columnas[i]] == "\033[40m  \033[0m": #Se evalua si la casilla esta vacia
                       print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Casilla Vacia")
                  elif tablero[filas[i]][columnas[i]].strip() in pblancas:#Se evalua si la pieza que esta en la casilla es del otro color del caballo
                       indice = pblancas.index(tablero[filas[i]][columnas[i]].strip())#Se obtiene que pieza es por medio del .index segun la lista de piezas del otro color del caballo
                       #De acuerdo a que pieza sea, se imprime en pantalla junto con el movimiento y la pieza con Unicode
                       if indice == 0:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Jaque")
                       elif indice == 1:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Reina blanca - {pblancas[indice]}")
                       elif indice ==2:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Alfil blanco - {pblancas[indice]}")
                       elif indice ==3:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Torre blanca - {pblancas[indice]}")
                       elif indice ==4:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Caballo blanco - {pblancas[indice]}")
                       elif indice ==5:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Peon blanco - {pblancas[indice]}")

    else: #El caballo es blanco
        for i in range(0,8):#Ciclo for para analizar cada uno de los posibles 8 movimientos
             if vf[i] == True:#Si existe la casilla se evalua el movimiento
                  if tablero[filas[i]][columnas[i]] == "\033[47m  \033[0m" or tablero[filas[i]][columnas[i]] == "\033[40m  \033[0m":#Se evalua si la casilla esta vacia
                       print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Casilla Vacia")
                  elif tablero[filas[i]][columnas[i]].strip() in pnegras:#Se evalua si la pieza que esta en la casilla es del otro color del caballo
                       indice = pnegras.index(tablero[filas[i]][columnas[i]].strip())#Se obtiene que pieza es por medio del .index segun la lista de piezas del otro color del caballo
                       #De acuerdo a que pieza sea, se imprime en pantalla junto con el movimiento y la pieza con Unicode
                       if indice == 0:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Jaque")
                       elif indice == 1:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Reina negra - {pnegras[indice]}")
                       elif indice ==2:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Alfil negro - {pnegras[indice]}")
                       elif indice ==3:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Torre negra - {pnegras[indice]}")
                       elif indice ==4:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Caballo negro - {pnegras[indice]}")
                       elif indice ==5:
                            print(f"{letras[columnas[i]]}{misfilas[filas[i]]} - Con Peon negro - {pnegras[indice]}")

def main():
    #Se define el numero de columnas y filas que tendra el tablero
    filas = 8
    columnas = 8
    #Se crea una tabla con valores vacios del tamaño de las columnas y filas
    tablero = [[None] * columnas for _ in range(filas)]
    #Se guarda en un arreglo las piezas blancas y negras utilizado Unicode
    pblancas = ["\u265A","\u265B","\u265D","\u265C","\u265E","\u265F"]
    pnegras = ["\u2654","\u2655","\u2657","\u2656","\u2658","\u2659"]
    imprimirtableroinicial(tablero)
    agregarpiezas(tablero,pnegras,pblancas)
    imprimirtablerio(tablero)
    print("Presione enter para proseguir a ingresar el caballo a evaluar")
    input()
    agregarcaballo(tablero,pnegras,pblancas)


if __name__ == "__main__":
    main()
