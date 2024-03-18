#VARIABLES NUMÉRICAS
entero1 = 1
entero2 = 2
entero3 = 3
entero4 = 4
decimal1 = 1.1
decimal2 = 2.2
decimal3 = 3.3
decimal4 = 4.4

#OPERACIONES
suma1 = entero1 + entero2
suma2 = entero1+ entero2 + entero3
suma3 = entero1 + decimal1
resta1 = entero4 - entero2
resta2 = decimal4 - entero4 #Debería dar 0.4 pero da 0.40000000000000036
multiplicacion1 = entero2 * entero3
multiplicacion2 = entero3 * decimal3 #Debería dar 9.9 pero da 9.899999999999999
division1 = entero4 / entero2
division2 = entero3 / entero2
division3 = decimal4 / decimal2
division4 = decimal3 / entero3 #Debería dar 1.1 pero da 1.0999999999999999

#IMPRIMIR LOS RESULTADOS DE LAS OPERACIONES
print("El resultado de suma1 es:" , suma1)
print("El resultado de suma2 es:" , suma2)
print("El resultado de suma3 es:" , suma3)
print("_____________________________________________________________")
print()
print("El resultado de resta1 es:" , resta1)
print("El resultado de resta2 es:" , resta2)
print("_____________________________________________________________")
print()
print("El resultado de multiplicacion1 es:" , multiplicacion1)
print("El resultado de multiplicacion2 es:" , multiplicacion2)
print("_____________________________________________________________")
print()
print("El resultado de division1 es:" , division1)
print("El resultado de division2 es:" , division2)
print("El resultado de division3 es:" , division3)
print("El resultado de division4 es:" , division4)
print("_____________________________________________________________")
print()

#EXPONENTE Y DIVISIÓN EXACTA
exponente1 = 2**2
exponente2 = 2**3
exponente3 = 2**4
print("El resultado del exponente1 es:" , exponente1)
print("El resultado del exponente2 es:" , exponente2)
print("El resultado del exponente3 es:" , exponente3)
print()

divisionExacta1 = decimal3//entero3
print("El resultado de la división exacta es:" , divisionExacta1) #El resultado es 1.1 por lo que imprime 1.0
print("_____________________________________________________________")
print()

#TEXTOS
print("Hola " * 4) #Imprime 4 veces seguidas el texto
# print("Hola" - "a") --> Solo se pueden sumar o multiplicar (concatener Strings)
print("_____________________________________________________________")
print()

#OPERACIONES RELACIONALES Y LÓGICAS
print("¿ 5 es mayor que 6 ? -->" , 5>6)
print("¿ 5 es menor que 6 ? -->" , 5<6)
print("¿ 5 es igual que 6 ? -->" , 5==6)
print("¿ 5 es mayor o igual que 6 ? -->" , 5>=6)
print("¿ 5 es menor o igual que 6 ? -->" , 5<=6)
print("¿ 5 es mayor que 4 y que 3 ?" , 5>4 and 5>3)
print("¿ 5 es mayor que 4 o que 6 ?" , 5>4 or 5>6)
print("¿ 5 es mayor que 4 y que 3 y no mayor que 6?" , 5>4 and 5>3 and not 5>6)
print("_____________________________________________________________")
print()


#IMPRESIONES
variable1 = "Hola me llamo Adrian"
print(variable1 , variable1, sep=" -- " , end="** \n")
print(variable1  , end=" FINAL")

