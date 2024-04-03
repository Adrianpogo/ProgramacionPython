import random as rd

posicionSerpiente = [[0,0],[0,1],[0,2],[0,3]]

direcciones = [
    (1, 0), #Derecha
    (0, 1), #Abajo
    (-1, 0), #Izquierda
    (0, -1) ] #Arriba

#Función para crear el tablero con las posiciones iniciales de la serpiente
def crearTablero(tamaño) :
    tablero = []
    posicion = []
    for j in range(tamaño):
        fila=[]
        for i in range(tamaño):
            posicion=[j,i]
            if posicion not in posicionSerpiente:
                fila.append(" ")
            elif posicion==posicionSerpiente[0]:
                fila.append("<")
            elif posicion==posicionSerpiente[-1]:
                fila.append("O")
            else:
                fila.append("=")
        tablero.append(fila)
    return tablero

#Función para imprimir el tablero
def imprimirTablero(tablero):
    print("  0 1 2 3 4 5 6 7")
    posicion=0
    for fila in tablero:
        print(posicion, end=" ")
        for elem in fila:
            print(elem,end=" ")
        posicion+=1
        print()
    print()

#Función para mover las posiciones de la serpiente
def moverse (direccion):
    #Añadimos la nueva posicion al array y elimno la ultima
    nuevaCabeza=[posicionSerpiente[-1][0]+direccion[1], posicionSerpiente[-1][1]+direccion[0]]
    posicionSerpiente.append(nuevaCabeza)
    posicionSerpiente.pop(0)


#Función para generar una dirección y comprobar que la serpiente se puede mover en esa direccion
#No se puede mover si:
#   -Se sale del tablero (por arriba o por abajo)
#   -Se mueve en la dirección en la que está el cuerpo
def comprobarDireccion(tablero):
    direccion = rd.choice(direcciones)

    #Comprobamos el resultdo de la suma de la dirección a la posición de la cabeza de la serpiente
    nuevaCabeza=[posicionSerpiente[-1][0]+direccion[1], posicionSerpiente[-1][1]+direccion[0]]

    if (nuevaCabeza[0] < 0 
        or nuevaCabeza[0] > len(tablero)-1 
        or nuevaCabeza[1] < 0 
        or nuevaCabeza[1] > len(tablero)-1
        or nuevaCabeza in posicionSerpiente[1:len(posicionSerpiente)]):
        
        return False

    else:
        print(">> Se mueve en la direccion", direccion)
        moverse(direccion)
        return True
        

#Función con el bucle principal del juego
def jugar ():
    #Se crea el tablero de 8x8 con la serpiente
    contador = 0
    tablero = crearTablero(8)
    while contador<10:
        if comprobarDireccion(tablero):
            print("\n>>> TURNO", contador, "<<<")
            tablero = crearTablero(8)
            imprimirTablero(tablero)
            contador += 1

#LLamada al juego
jugar()