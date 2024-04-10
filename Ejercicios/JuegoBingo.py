import random as rd

jugadores = {"Jugador1": [], "Jugador2": [], "Jugador3": []}

listaNumeros = []

def generarNums(inicio, fin):
    for i in range(2):
        numero1 = rd.randint(inicio, fin)
        numero2 = rd.randint(inicio, fin)
    if numero1 == numero2:
        return generarNums(inicio, fin)
    else:
        return numero1, numero2

def generarCarton():
    carton = []
    inicio = 1
    final = 9
    for i in range(9):
        num1, num2 = generarNums(inicio, final)
        carton.append(num1)
        carton.append(num2)
        if final < 89:
            inicio += 10
            final += 10
        else:
            inicio += 1
            final += 1

    carton.sort()
    return carton

def generarJugadores():
    for k, v in jugadores.items():
        if k == "Jugador1":
            v.append(generarCarton())
            v.append(generarCarton())
            v.append(generarCarton())
        if k == "Jugador2":
            v.append(generarCarton())
            v.append(generarCarton())
        if k == "Jugador3":
            v.append(generarCarton())

def generarNumero():
    numero = rd.randint(1, 90)
    if listaNumeros.__contains__(numero):
        return generarNumero()
    else:
        listaNumeros.append(numero)

def comprobarGanador():
    for jugador, cartones in jugadores.items():
        for carton in cartones:
            if set(carton).issubset(set(listaNumeros)):
                return jugador, carton
    return None

def jugar():
    generarJugadores()
    print("¡El juego de bingo ha comenzado!")
    carton_ganador = None

    while True:
        generarNumero()
        resultado = comprobarGanador()
        if resultado:
            ganador, carton_ganador = resultado
            for jugador, cartones in jugadores.items():
                for carton in cartones:
                    print(f"El jugador {jugador} tiene los siguientes números: {carton}")
            print("Lista de números que han salido:")
            print(listaNumeros)
            print(f"¡Tenemos un ganador! El ganador es {ganador} con el carton {carton_ganador}")
            break

jugar()

