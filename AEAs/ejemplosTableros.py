tableroSudoku1=[
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]
tableroSudoku2=[
    [5,3,9,8,7,6,4,1,2],
    [7,2,8,3,1,4,9,6,5],
    [6,4,1,2,9,5,7,3,8],
    [4,6,2,5,3,9,8,7,1],
    [3,8,5,7,2,1,6,4,9],
    [1,9,7,4,6,8,2,5,3],
    [2,5,6,1,8,7,3,9,4],
    [9,1,3,6,4,2,5,8,7],
    [8,7,4,9,5,3,1,2,6]
]
tableroSudoku3=[
    [5,3,9,8,7,6,4,1,1],
    [7,2,8,3,1,4,9,6,5],
    [6,4,1,2,4,5,7,3,8],
    [4,6,2,5,3,9,8,7,1],
    [3,8,5,7,2,1,6,4,9],
    [1,9,7,4,6,8,2,5,3],
    [2,5,6,1,8,3,3,9,4],
    [9,1,3,6,4,2,5,8,7],
    [8,7,4,9,5,3,1,2,6]
]

tablero3EnRaya1=[
    ['X','X','O'],
    ['','X','O'],
    ['','','O']
]
tablero3EnRaya2=[
    ['X','O','X'],
    ['O','X','O'],
    ['O','X','O']
]
tablero3EnRaya3=[
    ['X','X','O'],
    ['O','X','X'],
    ['O','O','X']
]



def comprobarSudoku(tablero):
    numeros = {1,2,3,4,5,6,7,8,9}
 
    #Comprobar Tablero lleno
    for fila in tablero:
        if not len(fila)==9:
            print("El tablero del sudoku no está completo")

    # Comprobar Horizontales --> Se convierte la fila a un set y se compara con el set de números
    # si no son iguales significa que el tablero está mal resuelto
    for fila in tablero:
        if not set(fila) == numeros :
            print("Hay algún número incorrecto --> Has perdido\n")
            return
            
    # Comprobar Verticales --> Guardamos en una lista los elementos de la vertical para posteriomente
    # convertirlos en set y compararlo con el set de números, si no son iguales está mal resulta
    numerosVerticales = []
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            numerosVerticales.append(tablero[j][i])
        if not numeros == set(numerosVerticales):
            print("Hay algún número incorrecto --> Has perdido\n")
            return
        numerosVerticales.clear()

    # Comprobar secciones 3x3
    # Añado a una lista todos los centros de las secciones existentes (9),
    # con la lista de direcciones se añaden todos los números vecinos a una lista 
    # que se convertirá en un set para compararlo con el set de números
    direcciones=[(1,0),(1,1),(0,1),(0,-1), (-1,0),(-1,-1),(-1,1), (1,-1)]
    posiciones =[[1,1], [1,4], [1,7], [4,1], [4,4], [4,7], [7,1] ,[7,4], [7,7]]

    for posicion in posiciones :
        numerosCuadrado = []
        numerosCuadrado.append(tablero[posicion[0]][posicion[1]])
        for direccion in direcciones:
            numerosCuadrado.append(tablero[posicion[0]+direccion[0]][posicion[1]+direccion[1]])
        if not set(numerosCuadrado) == numeros:
            print("Hay algún número incorecto --> Has perdido\n")
            return
    print("Has resuelto el Sudoku, enhorabuena! --> Has ganado\n")


def comprobar3EnRaya(tablero):

    # Siempre que se encuentre un ganador se convierte en True, de forma que al final de la función
    # si sigue siendo False significará que ninguno ha ganado
    # El número de fichas totales es 9, si el número es menor significará que la partida sigue en curso
    numeroXs = tablero[0].count("X")+ tablero[1].count("X") + tablero[2].count("X")  
    numeroOs = tablero[0].count("O") + tablero[1].count("O")+ tablero[2].count("O")
    numeroFichas = numeroXs + numeroOs

    # Comprobar Filas --> Almaceno el primer elemento de cada fila y compruebo que los 2 siguentes sean iguales
    for fila in tablero:
        elemento = fila[0]
        if (elemento == "X" or elemento== "O") and elemento == fila[1] and elemento == fila[2]:
            print("Ha ganado '", elemento, "' --> Fila\n",)
            return

    # Comprobar Columnas --> Uso un contador para almacenar el número de elementos iguales
    # Cúando el contador sea 3 significa que los elementos de una columna son todos iguales
    contador = 0
    for i in range(3):
        elemento = tablero[0][i]
        if elemento == "X" or elemento== "O":
            for j in range(3):
                if tablero[j][i] == elemento:
                    contador +=1
                    if contador == 3:
                        print("Ha ganado '", elemento, "' --> Columna\n",)
                        return
            contador = 0

    # Comprobar Diagonal Derecha
    elemento = tablero[0][0]
    if (elemento == "X" or elemento== "O") and elemento == tablero [1][1] and elemento == tablero[2][2]:
        print("Ha ganado '", elemento, "' --> Diagonal derecha\n",)
        return
        

    # Comprobar Diagonal Izquierda
    elemento = tablero[0][2]
    if (elemento == "X" or elemento== "O") and elemento == tablero [1][1] and elemento == tablero[2][0]:
        print("Ha ganado '", elemento, "' --> Diagonal izquierda\n",)
        return

    # Comprobar si no hay ganador o la partida sigue en curso
    if numeroFichas < 9:
        print("No hay un ganador --> La partida sigue en curso\n")
    else:
        print("No hay un ganador --> Empate\n")




print("Para el tablero 1 de 3 en Raya:")
comprobar3EnRaya(tablero3EnRaya1)
print("Para el tablero 2 de 3 en Raya:")
comprobar3EnRaya(tablero3EnRaya2)
print("Para el tablero 3 de 3 en Raya:")
comprobar3EnRaya(tablero3EnRaya3)
print("Para el tablero 1 Sudoku:")
comprobarSudoku(tableroSudoku1)
print("Para el tablero 2 Sudoku:")
comprobarSudoku(tableroSudoku2)
print("Para el tablero 3 Sudoku:")
comprobarSudoku(tableroSudoku3)

