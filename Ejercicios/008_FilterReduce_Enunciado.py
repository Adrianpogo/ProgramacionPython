from functools import reduce

# Ejercicio 1
# 1. Multiplicar todos los elementos de una lista por 3:

print(">>> EJERCICIO 1")
lista_original = [1, 2, 3, 4, 5]
print("Elemento original -->", lista_original)

listax3 = list(map(lambda x: x*3, lista_original))

print("Nuevo elemento -->", listax3)

print("\n--------------------------------------\n")



# Ejercicio 2
# 2. Filtrar los números pares de una lista:
print(">>> EJERCICIO 2")
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Elemento original -->", lista_numeros)

listaPares = list(filter(lambda x: x%2==0, lista_numeros))

print("Nuevo elemento -->", listaPares)
print("\n--------------------------------------\n")

# Ejercicio 3
# 3. Sumar todos los elementos de una lista:
print(">>> EJERCICIO 3")
lista_numeros = [1, 2, 3, 4, 5]
print("Elemento original -->", lista_numeros)

lista_sum = reduce(lambda x,y: x+y, lista_numeros)

print("Nuevo elemento -->", lista_sum)
print("\n--------------------------------------\n")

# Ejercicio 4
# 4. Filtrar los números mayores que 10 y multiplicarlos por 2:
print(">>> EJERCICIO 4")
lista_numeros = [5, 10, 15, 20, 25]
print("Elemento original -->", lista_numeros)

l_filtrada = list(filter(lambda x: x>=10, lista_numeros))
l_map = list(map(lambda x: x*2, l_filtrada))
print("Nuevo elemento -->", l_map)
print("\n--------------------------------------\n")

# Ejercicio 5
# 5. Filtrar las palabras que tienen más de 5 letras en una lista de palabras:
print(">>> EJERCICIO 5")
lista_palabras = ["py", "prog", "aprendizaje", "desarrollo", "informatica"]
print("Elemento original -->", lista_palabras)

l_filtrada = list(filter(lambda x: len(x)>5 , lista_palabras))

print("Nuevo elemento -->", l_filtrada)
print("\n--------------------------------------\n")

# Ejercicio 6
# 6. Calcular el producto de todos los elementos de una lista:
print(">>> EJERCICIO 6")
lista_numeros = [1, 2, 3, 4, 5]
print("Elemento original -->", lista_numeros)

producto = reduce(lambda x,y: x*y, lista_numeros)

print("Nuevo elemento -->", producto)
print("\n--------------------------------------\n")

# Ejercicio 7
# 7. Convertir todas las palabras en una lista a mayúsculas:
print(">>> EJERCICIO 7")
lista_palabras = ["hola", "python", "mundo", "programacion"]
print("Elemento original -->", lista_palabras)

l_map = list(map(lambda x: x.upper(), lista_palabras))

print("Nuevo elemento -->", l_map)
print("\n--------------------------------------\n")

# Ejercicio 8
# 8. Filtrar los números impares y elevarlos al cuadrado:
print(">>> EJERCICIO 8")
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Elemento original -->", lista_numeros)

l_filtrada= list(filter(lambda x: not x%2==0, lista_numeros))
l_map= list(map(lambda x: x**2, l_filtrada))

print("Nuevo elemento -->", l_map)
print("\n--------------------------------------\n")

# Ejercicio 9
# 9. Concatenar todas las palabras de una lista separadas por un guión:
print(">>> EJERCICIO 9")
lista_palabras = ["hola", "python", "mundo"]
print("Elemento original -->", lista_palabras)

l_unida = reduce(lambda x, y: x + "-" + y, lista_palabras)

print("Nuevo elemento -->", l_unida)
print("\n--------------------------------------\n")

# Ejercicio 10
# 10. Filtrar los elementos de una lista que son cadenas de texto:
print(">>> EJERCICIO 10")
lista_mixta = [1, "python", 3.5, "programacion", True, "aprendizaje"]
print("Elemento original -->", lista_mixta)

l_filtrada=list(filter(lambda x: x.__class__.__name__ == "str",lista_mixta))

print("Nuevo elemento -->", l_filtrada)
print("\n--------------------------------------\n")

# Ejercicio 11
# 11. Multiplicar los elementos de dos listas elemento por elemento:
print(">>> EJERCICIO 11")
lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 3, 4, 5, 6]
print("Elemento original -->", lista1)
print("Elemento original -->", lista2)

resultado_ejercicio11 = list(map(lambda x, y: x * y, lista1, lista2))
print("Nuevo elemento -->", resultado_ejercicio11)
print("\n--------------------------------------\n")


# Ejercicio 12
# 12. Filtrar los números negativos de una lista y convertirlos a positivos:
print(">>> EJERCICIO 12")
lista_numeros = [-5, 10, -15, 20, -25]
print("Elemento original -->", lista_numeros)

resultado_ejercicio12 = list(map(lambda x: abs(x), filter(lambda x: x < 0, lista_numeros)))
print("Nuevo elemento -->", resultado_ejercicio12)
print("\n--------------------------------------\n")


# Ejercicio 13
# 13. Filtrar las palabras que comienzan con una letra específica de una lista:
print(">>> EJERCICIO 13")
letra_busqueda = 'p'
lista_palabras = ["python", "programacion", "aprendizaje", "desarrollo", "informatica"]
print("Elemento original -->", lista_palabras)

resultado_ejercicio13 = list(filter(lambda palabra: palabra.startswith(letra_busqueda), lista_palabras))
print("Nuevo elemento -->", resultado_ejercicio13)
print("\n--------------------------------------\n")

# Ejercicio 14
# 14. Sumar los números pares de una lista:
print(">>> EJERCICIO 14")
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Elemento original -->", lista_numeros)

resultado_ejercicio14 = reduce(lambda x, y: x + y, filter(lambda x: x % 2 == 0, lista_numeros))
print("Nuevo elemento -->", resultado_ejercicio14)
print("\n--------------------------------------\n")

# Ejercicio 15
# 15. Filtrar los números primos de una lista de números:
print(">>> EJERCICIO 15")
lista_numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("Elemento original -->", lista_numeros)

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

resultado_ejercicio15 = list(filter(es_primo, lista_numeros))
print("Nuevo elemento -->", resultado_ejercicio15)
print("\n--------------------------------------\n")

# Ejercicio 16
# 16. Concatenar solo las palabras que tienen más de 3 letras en una lista:
print(">>> EJERCICIO 16")
lista_palabras = ["hola", "python", "mundo", "programacion", "ai", "openai"]
print("Elemento original -->", lista_palabras)

resultado_ejercicio16 = list(filter(lambda x: len(x) > 3, lista_palabras))
print("Nuevo elemento -->", resultado_ejercicio16)
print("\n--------------------------------------\n")

# Ejercicio 17
# 17. Calcular el promedio de los elementos de una lista de números:
print(">>> EJERCICIO 17")
lista_numeros = [1, 2, 3, 4, 5]
print("Elemento original -->", lista_numeros)

suma = reduce(lambda x, y: x + y, lista_numeros)
promedio = suma / len(lista_numeros)
print("Nuevo elemento -->", promedio)
print("\n--------------------------------------\n")

# Ejercicio 18
# 18. Crear una lista de tuplas que contengan el número y su factorial:
print(">>> EJERCICIO 18")
lista_numeros = [1, 2, 3, 4, 5]
print("Elemento original -->", lista_numeros)

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

resultado_ejercicio18 = list(map(lambda x: (x, factorial(x)), lista_numeros))
print("Nuevo elemento -->", resultado_ejercicio18)
print("\n--------------------------------------\n")

# Ejercicio 19
# 19. Calcular la suma de los dígitos de una lista de números:
print(">>> EJERCICIO 19")
lista_numeros = [123, 456, 789, 101112]
print("Elemento original -->", lista_numeros)

def suma_digitos(n):
    return reduce(lambda x, y: int(x) + int(y), str(n))

resultado_ejercicio19 = list(map(suma_digitos, lista_numeros))
print("Nuevo elemento -->", resultado_ejercicio19)
print("\n--------------------------------------\n")

