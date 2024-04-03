import random as rd
pos=[(0,1),(0,-1),(1,0),(-1,0)]
serpiente=[[0,0],[0,1],[0,2],[0,3]]
posComida=[]


def generarComida():
    posComida.clear()
    x = rd.randint(0,4)
    y = rd.randint(0,4)
    posicion=[x,y]
    if posicion not in serpiente:
        posComida.append(posicion)
    else:
        generarComida()


def posValida(posVector):
    nuevaCabeza=serpiente[-1].copy()
    nuevaCabeza[0]+=posVector[0]
    nuevaCabeza[1]+=posVector[1]
    if (nuevaCabeza[0]>=0 and nuevaCabeza[0]<5 #que la posición X este dentro del tablero
        and nuevaCabeza[1]>=0 and nuevaCabeza[1]<5 #que la posición Y este dentro del tablero
        and (nuevaCabeza not in serpiente or nuevaCabeza == serpiente[0]) #que no se coma el cuerpo pero si la cola
    ):
        return True, nuevaCabeza
    else:
        return False, nuevaCabeza
    
    
def imprimir():
    tablero=[]
    for x in range(0,5):
        aux=[' ']*5
        tablero.append(aux)
    
    print("  0 1 2 3 4 ")
    for x in range(0,5):
        print(x, end=" ")
        for y in range(0,5):
            posicion = [x,y]
            if posicion not in serpiente:
                print(" ", end=" ")
            elif posicion == serpiente[0]:
                print("<", end=" ")
            elif posicion == serpiente[-1]:
                print("O", end=" ")
            elif posicion == posComida:
                print("X", end=" ")
            else:
                print("=", end=" ")
        print(" ")
        
        
        
        
def mover(posVector):
    valido,nuevaCabeza= posValida(posVector)
    if valido:
        if nuevaCabeza in posComida:
            serpiente.append(nuevaCabeza)
            generarComida()
            imprimir()
            print()
        else:
            serpiente.append(nuevaCabeza)
            serpiente.pop(0)
            imprimir()
            print()
    else:
        print("-- Movimiento invalido")


'''
>>>>> EJECUCIÓN DEL JUEGO <<<<<
'''
print("\n>> TURNO 0")
generarComida()
imprimir()
for x in range(100):
    print("\n>> TURNO", x)
    mover(pos[rd.randrange(4)])