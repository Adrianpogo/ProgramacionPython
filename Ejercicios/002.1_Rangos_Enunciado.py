import string 

"""
Ejercicio 1: Creación de un Rango Simple
Define un rango que vaya desde 0 hasta 5 (inclusive).
Imprime el rango creado.
"""

print("\n>> EJERCICIO 1")
print()

print("Rango [0,5]:" , list(range(6)))

print("-------------------------------------------")
print()

"""
Ejercicio 2: Creación de un Rango con Inicio y Fin Específicos
Define un rango que vaya desde 5 hasta 10 (inclusive).
Imprime el rango creado.
"""

print("\n>> EJERCICIO 2")
print()

print("Rango [5,10]:" , list(range(5,11)))

print("-------------------------------------------")
print()

"""
Ejercicio 3: Creación de un Rango con Incremento Específico
Define un rango que vaya desde 1 hasta 10 (inclusive) con incremento de 2.
Imprime el rango creado.
"""

print("\n>> EJERCICIO 3")
print()

print("Rango [1,10] con incremento de 2:" , list(range(1,11,2)))

print("-------------------------------------------")
print()


"""
Ejercicio 4: Iteración sobre un Rango Simple
Itera sobre un rango que vaya desde 0 hasta 3 (inclusive).
Imprime cada valor del rango en una línea separada.
"""

print("\n>> EJERCICIO 4")
print()

print("Elementos de un rango [0,3]")
for i in range(4):
    print("Elemento" , i)

print("-------------------------------------------")
print()

"""
Ejercicio 5: Iteración sobre un Rango con Incremento Específico
Itera sobre un rango que vaya desde 0 hasta 10 (inclusive) con incremento de 2.
Imprime cada valor del rango en una línea separada.
"""

print("\n>> EJERCICIO 5")
print()

print("Elementos de un rango [0,10] con incremento de 2")
for i in range(0,11,2):
    print("Elemento" , i)

print("-------------------------------------------")
print()

"""
Ejercicio 6: Uso de Rangos en Funciones de Control de Flujo
Itera sobre un rango que vaya desde 10 hasta 1 (inclusive) con decremento de 1.
Imprime cada valor del rango en una línea separada.
"""

print("\n>> EJERCICIO 6")
print()

print("Elementos de un rango [1,10] con decremento ")
for i in range(10,0,-1):
    print("Elemento" , i)

print("-------------------------------------------")
print()

"""
Ejercicio 7: Uso de Rangos en Condicionales
Verifica si un número ingresado por el usuario está dentro de un rango predefinido.
"""

print("\n>> EJERCICIO 7")
print()

numero = 5

if numero in range(0,10):
    print(numero , "está entre 0 y 9")
else:
    print(numero , "no está entre 0 y 9")

print("-------------------------------------------")
print()

"""
Ejercicio 8: Uso de Rangos para Generar Secuencias de Números
Genera una lista de números pares en el rango de 0 a 10 (inclusive).
Imprime la lista resultante.
"""

print("\n>> EJERCICIO 8")
print()

print("Números pares entre [1,10] :" , list(range(1,11,2)))

print("-------------------------------------------")
print()

"""
Ejercicio 9: Uso de Rangos para Sumar Elementos
Calcula la suma de todos los números en el rango de 1 a 100 (inclusive).
Imprime el resultado de la suma.
"""

print("\n>> EJERCICIO 9")
print()

sumatorio=0

for i in range(1,101):
    sumatorio += i

print("La suma de los elementos en el rango[1,100] es:" , sumatorio)

print("-------------------------------------------")
print()

"""
Ejercicio 10: Uso de Rangos para Contar Elementos
Cuenta cuántos números pares hay en el rango de 1 a 50 (inclusive).
Imprime el total de números pares.
"""

print("\n>> EJERCICIO 10")
print()

contador = len(list(range(1,51,2)))

print("El número de números pares entre 1 y 50 es:" , contador)

print("-------------------------------------------")
print()

"""
Ejercicio 11: Uso de Rangos en una Función
Define una función llamada `imprimir_rango` que reciba un parámetro `limite`.
La función debe imprimir todos los números desde 0 hasta el `limite` (inclusive) utilizando un rango.
"""

print("\n>> EJERCICIO 11")
print()

def imprimir_rango (limite):
    return(list(range(limite+1)))

print("Para un límite de 8 el rango es:" , imprimir_rango(8))

print("-------------------------------------------")
print()

"""
Ejercicio 12: Uso de Rangos en una Función con Paso Personalizado
Define una función llamada `imprimir_rango_paso` que reciba tres parámetros: `inicio`, `fin` y `paso`.
La función debe imprimir todos los números desde `inicio` hasta `fin` (inclusive) utilizando un rango con el paso especificado.
"""

print("\n>> EJERCICIO 12")
print()

def imprimir_rango_paso(inicio, fin, paso):
    numeros = list()
    i=1
    while i in range(inicio, fin+1):
        numeros.append(i)
        i+=2
    
    return numeros

print("Para el rango [1,10,2] el resultado es:" , imprimir_rango_paso(1,10,2))

print("-------------------------------------------")
print()

"""
Ejercicio 13: Uso de Rangos para Generar Secuencias de Caracteres
Genera una lista de letras del alfabeto inglés (minúsculas) utilizando un rango.
Imprime la lista resultante.
"""

print("\n>> EJERCICIO 13")
print()

alfabeto = []
for letra in range (97, 123):
    alfabeto.append(chr(letra))

print(alfabeto)


print("-------------------------------------------")
print()

"""
Ejercicio 14: Uso de Rangos para Generar Patrones
Genera un patrón numérico en forma de triángulo utilizando un rango y la función `join()`.
".".join(elemento) --> hace que los elementos dentro del elemento se unan con .
Imprime el patrón resultante.
"""

print("\n>> EJERCICIO 14")
print()


for i in range(1, 11):
    numeros = list()
    for num in range(1, i + 1):
        numeros.append(str(num))
    print(' '.join(numeros))


print("-------------------------------------------")
print()

"""
Ejercicio 15: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón numérico en forma de triángulo invertido utilizando un bucle for.
Imprime el patrón resultante.
"""

print("\n>> EJERCICIO 15")
print()

for i in range(10, 0, -1):
    numeros = list()
    for num in range(i, 0, -1):
        numeros.append(str(num))
    print(' '.join(numeros))

print("-------------------------------------------")
print()

"""
Ejercicio 16: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de asteriscos en forma de pirámide utilizando un bucle for.
Imprime el patrón resultante.
"""

print("\n>> EJERCICIO 16")
print()

altura = 5

for i in range(altura):
    espacios = " " * (altura - i - 1)
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)


print("-------------------------------------------")
print()

"""
Ejercicio 17: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de números en forma de diamante utilizando un bucle for.
Imprime el patrón resultante.
"""

print("\n>> EJERCICIO 17")
print()

altura = 10

# Parte superior del diamante
for i in range(1, altura + 1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)

# Parte inferior del diamante
for i in range(altura - 1, 0, -1):
    espacios = " " * (altura - i)
    asteriscos = "*" * (2 * i - 1)
    print(espacios + asteriscos)


print("-------------------------------------------")
print()

"""
Ejercicio 18: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de letras en forma de pirámide utilizando un bucle for.
Imprime el patrón resultante.
"""

print("\n>> EJERCICIO 18")
print()

altura = 5

for i in range(altura):
    espacios = " " * (altura - i - 1)
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)

print("-------------------------------------------")
print()

"""
Ejercicio 19: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de letras en forma de pirámide invertida utilizando un bucle for.
Imprime el patrón resultante.
"""

print("\n>> EJERCICIO 19")
print()

letras = ["A" , "B" , "C" , "D" , "E"]

for i in range(altura):
    espacios = " " * (altura - i - 1)
    letras_piramide = ""
    for j in range(i + 1):
        letras_piramide += letras[j]
    print(espacios + ' '.join(letras_piramide))

print("-------------------------------------------")
print()

"""
Ejercicio 20: Uso de Rangos para Generar Patrones (Otra Forma)
Genera un patrón de letras en forma de diamante utilizando un bucle for.
Imprime el patrón resultante.
"""

print("\n>> EJERCICIO 20")
print()

altura = 5
letras = string.ascii_uppercase

#Parte superior del diamante
for i in range(altura):
    espacios = " " * (altura - i - 1)
    letras_piramide = ""
    for j in range(i + 1):
        letras_piramide += letras[j]
    print(espacios + ' '.join(letras_piramide))

#Parte inferior del diamante
for i in range(altura - 1, 0, -1):
    espacios = " " * (altura - i)
    letras_piramide = ""
    for j in range(i):
        letras_piramide += letras[j]
    print(espacios + ' '.join(letras_piramide))
    
print("-------------------------------------------")
print()
