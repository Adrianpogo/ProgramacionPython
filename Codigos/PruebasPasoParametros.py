'''
Tradicionalmente (es como en JAVA):

    - Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
    - Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...

'''

'''
    ========================================================
    \                                                      |
    \                   PASO POR VALOR                     |
    \                                                      |
    ========================================================
'''
#PRUEBA CON NÚMEROS ENTEROS (FUNCIONA IGUAL CON LOS DATOS NUMÉRICOS)
def doblar_valor(numero):
    numero *= 2
    return numero

n = 10
print(doblar_valor(n)) #20
print(n) #10

#-------------------------------------------------------------------------------

#PRUEBA CON BOOLEANOS
def esVerdad(valor):
    valor=True
    return valor

valor=False
print(esVerdad(valor)) #True
print(valor) #False

#-------------------------------------------------------------------------------

#PRUEBA CON CADENAS

def modificarPalabra (palabra):
    palabra += "Añadido"
    return palabra

palabra = "Palabra"
print(modificarPalabra(palabra)) #PalabraAñadido
print(palabra) #Palabra

'''
    ========================================================
    \                                                      |
    \                PASO POR REFERENCIA                   |
    \                                                      |
    ========================================================
'''