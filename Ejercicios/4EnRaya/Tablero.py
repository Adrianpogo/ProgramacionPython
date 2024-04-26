from Ficha import Ficha

class Tablero:
   
    def __init__(self, tamaño, equipo1, equipo2):
        self.tablero = []
        for _ in range(0, tamaño):
            aux=['-']*tamaño
            self.tablero.append(aux)
        self.listaEquipo=[equipo1,equipo2]
       
       
    def imprimir (self):
        for fila in self.tablero:
            for elem in fila:
                print(elem, end="")
            print()
           
    def colocarFicha(self, ficha, columna):
        for fila in range(len(self.tablero) -1, -1, -1):
            if self.tablero[fila][columna] == "-":
                self.tablero[fila][columna] = ficha.representacion
                return True
        return False
   
    def comprobarColumna(self,columna):
        if columna >= len(self.tablero) or columna < 0:
            return False
               
        if self.tablero[0][columna] == "-":
            return True
        return False
   
    def verificarGanador(self):
        for fila in range(len(self.tablero)):
            for columna in range(len(self.tablero[0]) -4):
                if self.tablero[fila][columna] != "-":
                    if self.tablero[fila][columna + 1] == self.tablero[fila][columna + 2] == self.tablero[fila][columna + 3]:
                        return True
       
        for columna in range(len(self.tablero)):
            for fila in range(len(self.tablero[0]) -4):
                if self.tablero[fila][columna] != "-":
                    if self.tablero[fila + 1][columna] == self.tablero[fila + 2][columna] == self.tablero[fila + 3][columna]:
                        return True
 
 
tablero = Tablero(5,"X", "O")
ganador = False
turno = 0
while not ganador:
    tablero.imprimir()
    columna = int(input("Introduce columna: "))
    ficha = Ficha(tablero.listaEquipo[turno])
       
    if tablero.comprobarColumna(columna):
        tablero.colocarFicha(ficha, columna)
        turno = (turno+1) % 2
        ganador = tablero.verificarGanador()
    else:
         print("Columna fuera de rango. Vuelvelo a escribir:")

    
        