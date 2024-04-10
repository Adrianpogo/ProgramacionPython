import random

# Direcciones posibles: (norte, sur, este, oeste)
direcciones = [(0, -1), (0, 1), (1, 0), (-1, 0)]

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    print("  0 1 2 3 4 5")
    posicion=0
    for fila in tablero:
        print(posicion, end=" ")
        for elem in fila:
            print(elem,end=" ")
        posicion+=1
        print()
    print()

# Función para crear el tablero con el Pacman, los fantasmas y las comidas
def crear_tablero(tamaño, num_fantasmas, num_comidas):
    # Inicializamos el tablero con todas las casillas vacías
    tablero = []
    for i in range(tamaño):
        fila = [] 
        for j in range(tamaño):
            fila.append(" ")
        tablero.append(fila)

    # Colocamos el Pacman en la esquina superior izquierda
    tablero[0][0] = "O"

    # Colocamos los fantasmas en posiciones aleatorias
    for _ in range(num_fantasmas):
        x = random.randint(0, tamaño - 1)
        y = random.randint(0, tamaño - 1)
        while tablero[y][x] != " ":
            x = random.randint(0, tamaño - 1)
            y = random.randint(0, tamaño - 1)
        tablero[y][x] = "X"

    # Colocamos las comidas en posiciones aleatorias
    for _ in range(num_comidas):
        x = random.randint(0, tamaño - 1)
        y = random.randint(0, tamaño - 1)
        while tablero[y][x] != " ":
            x = random.randint(0, tamaño - 1)
            y = random.randint(0, tamaño - 1)
        tablero[y][x] = "^"

    return tablero

# Función para mover al Pacman
def mover_pacman(tablero, direccion, puntos):
    tamaño = len(tablero)
    x, y = 0, 0  # Posición actual del Pacman

    # Buscamos la posición actual del Pacman en el tablero
    for i in range(tamaño):
        for j in range(tamaño):
            if tablero[i][j] == "@":
                x, y = j, i
                break

    # Calculamos la nueva posición
    nuevo_x = x + direccion[0]
    nuevo_y = y + direccion[1]

    # Verificamos si el movimiento es válido
    if (0 <= nuevo_x < tamaño) and (0 <= nuevo_y < tamaño) and (tablero[nuevo_y][nuevo_x] != "X"):
        # Si hay comida en la nueva posición, la comemos
        if tablero[nuevo_y][nuevo_x] == "^":
            puntos += 1
        # Movemos al Pacman
        tablero[y][x] = " "
        tablero[nuevo_y][nuevo_x] = "@"
    return puntos

# Creamos el tablero
tablero = crear_tablero(5, 3, 4)

# Inicializamos los puntos
puntos = 0

# Ejecutamos el juego
while puntos < 4:  # Se detiene cuando se hayan comido todas las comidas
    imprimir_tablero(tablero)
    print()
    direccion = random.choice(direcciones)
    puntos = mover_pacman(tablero, direccion, puntos)

print("¡Has comido todas las comidas!")
