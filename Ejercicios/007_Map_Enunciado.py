import math

# Ejercicio 1
#1. Multiplicar todos los elementos de una lista por 3:
print(">>> EJERCICIO 1")
lista_original = [1, 2, 3, 4, 5]
print("Lista original -->", lista_original)

def mult3 (elem):
    return elem*3

print("Nueva lista -->", list(map(mult3,lista_original)))

print("\n--------------------------------------\n")

# Ejercicio 2
#2. Convertir una lista de cadenas a mayúsculas:
print(">>> EJERCICIO 2")
lista_original = ['hola', 'mundo', 'python']
print("Lista original -->", lista_original)

print("Nueva lista -->", list(map(str.upper,lista_original)))

print("\n--------------------------------------\n")

# Ejercicio 3
#3. Calcular la raíz cuadrada de cada número en una lista y almacenar los resultados en un set:
print(">>> EJERCICIO 3")
lista_original = [4, 9, 16, 25]
print("Lista original -->", lista_original)

def raiz(elem):
    return elem**0.5

print("Nueva lista -->", set(map(raiz,lista_original)))

print("\n--------------------------------------\n")

# Ejercicio 4
#4. Duplicar las claves de un diccionario:
print(">>> EJERCICIO 4")
diccionario_original = {'a': 1, 'b': 2, 'c': 3}
print("Diccionario original -->", diccionario_original)

def duplicarClave(clave):
    return clave*2

print("Nuevo diccionario -->", list(map(duplicarClave,diccionario_original.keys())))

print("\n--------------------------------------\n")

# Ejercicio 5
#5. Elevar al cubo todos los valores de un diccionario:
print(">>> EJERCICIO 5")
diccionario_original = {'a': 2, 'b': 3, 'c': 4}
print("Diccionario original -->", diccionario_original)

def cuboValores(valor):
    return valor*2

print("Nuevo diccionario (valores) -->", list(map(cuboValores,diccionario_original.values())))

print("\n--------------------------------------\n")

# Ejercicio 6
#6. Concatenar un sufijo a cada cadena en una lista:
print(">>> EJERCICIO 6")
lista_original = ['apple', 'banana', 'orange']
print("Lista original -->", lista_original)

def sufijo (elem):
    return "#"+elem

print("Nueva lista -->", list(map(sufijo,lista_original)))

print("\n--------------------------------------\n")

# Ejercicio 7
#7. Calcular el cuadrado de cada número en una lista y almacenar los resultados en un conjunto:
print(">>> EJERCICIO 7")
lista_original = [2, 3, 4, 5]
print("Lista original -->", lista_original)

def cuadrado(elem):
    return elem**2

print("Nuevo conjunto -->", set(map(cuadrado, lista_original)))

print("\n--------------------------------------\n")

# Ejercicio 8
#8. Dividir por 2 todos los valores de un diccionario:
print(">>> EJERCICIO 8")
diccionario_original = {'a': 10, 'b': 20, 'c': 30}
print("Diccionario original -->", diccionario_original)

def dividirClave(clave):
    return clave/2

print("Nuevo diccionario -->", list(map(dividirClave,diccionario_original.values())))

print("\n--------------------------------------\n")

# Ejercicio 9
#9. Convertir cada número en una lista a su equivalente en binario y almacenar los resultados en una lista:
print(">>> EJERCICIO 9")
lista_original = [3, 6, 9, 12]
print("Lista original -->", lista_original)

def binario(numero):
    return bin(numero)

print(list(map(binario, lista_original)))


print("\n--------------------------------------\n")

# Ejercicio 10
#10. Eliminar las vocales de cada cadena en una lista:

print(">>> EJERCICIO 10")
lista_original = ['hello', 'world', 'python']
print("Lista original -->", lista_original)

def eliminar_vocales(elem):
    vocales = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    for vocal in vocales:
        elem = elem.replace(vocal, "")
    return elem
    
print("Nueva lista -->", list(map(eliminar_vocales,lista_original)))

print("\n--------------------------------------\n")


# Ejercicio 11
#11. Dada una lista de estudiantes con sus calificaciones, calcular el promedio 
#de cada estudiante y almacenar los resultados en un diccionario:
print(">>> EJERCICIO 11")
estudiantes_calificaciones = {'Juan': [85, 90, 95], 'María': [78, 82, 80], 'Pedro': [90, 92, 88]}
print("Diccionario original -->", estudiantes_calificaciones)

def calcular_promedio(estudiante):
    nombre, calificaciones = estudiante
    promedio = sum(calificaciones) / len(calificaciones)
    return nombre, promedio

promedios_estudiantes = dict(map(calcular_promedio, estudiantes_calificaciones.items()))
print("Diccionario de promedios -->", promedios_estudiantes)

print("\n--------------------------------------\n")

# Ejercicio 12
#12. En una lista de nombres, eliminar los nombres que contienen menos de 5 caracteres, 
#convertir los restantes a minúsculas y ordenarlos alfabéticamente:
print(">>> EJERCICIO 12")
lista_nombres = ['Ana', 'Carlos', 'Eva', 'Juan', 'Maria', 'Pedro', 'Luisa']
print("Lista original -->", lista_nombres)

def filtrarTamaño (elem):
    return len(elem) >=5

nombres_filtrados = list(filter(filtrarTamaño,lista_nombres))
print("Nueva lista -->", sorted(list(map(str.lower,nombres_filtrados))))

print("\n--------------------------------------\n")

# Ejercicio 13
#13. En un diccionario que contiene nombres de ciudades como claves y listas de temperaturas 
#como valores, calcular el promedio de temperaturas de cada ciudad y almacenar los resultados en un nuevo diccionario:
print(">>> EJERCICIO 13")
temperaturas_ciudades = {'Boston': [68, 72, 70], 'Los Angeles': [75, 80, 78], 'Miami': [82, 85, 80]}
print("Diccionario original -->", temperaturas_ciudades)

def temperatura_promedio(ciudad):
    nombre, temperatura = ciudad 
    promedio = sum(temperatura) / len(temperatura)
    return nombre, promedio

temperaturas_medias = dict(map(temperatura_promedio,temperaturas_ciudades.items()))
print("Nuevas temperatura -->", temperaturas_medias)

print("\n--------------------------------------\n")

# Ejercicio 14
#14. Dada una lista de números, convertir cada número en su equivalente en hexadecimal y almacenar los resultados en una lista:
print(">>> EJERCICIO 14")
lista_numeros = [10, 20, 30, 40, 50]
print("Lista original -->", lista_numeros)

def hexadecimal(numero):
    return hex(numero)

print(list(map(hexadecimal, lista_numeros)))

print("\n--------------------------------------\n")


# Ejercicio 15
#15. En una lista de palabras, eliminar las palabras que contienen la letra 'a', convertir 
#las restantes a mayúsculas y ordenarlas alfabéticamente:
print(">>> EJERCICIO 15")
lista_palabras = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear']
print("Lista original -->", lista_palabras)

def eliminar_a(elem):
    return elem.count('a')==0

palabras_sin_a = list(filter(eliminar_a,lista_palabras))
print("Nueva lista -->", sorted(list(map(str.upper,palabras_sin_a))))

print("\n--------------------------------------\n")

# Ejercicio 16
#16. Dada una lista de tuplas con nombres y edades, calcular la edad promedio y almacenar el resultado en un diccionario:
print(">>> EJERCICIO 16")
estudiantes_edades = [('Juan', 20), ('María', 22), ('Pedro', 19)]
print("Lista original -->", estudiantes_edades)



print("\n--------------------------------------\n")

# Ejercicio 17
#17. En una lista de oraciones, contar la cantidad de palabras en cada oración y almacenar los resultados en una lista:
print(">>> EJERCICIO 17")
lista_oraciones = ['Python es un lenguaje de programación.', 'Tiene una sintaxis sencilla y elegante.']
print("Lista original -->", lista_oraciones)

    

print("\n--------------------------------------\n")

# Ejercicio 18
#18. En un diccionario que contiene nombres de estudiantes como claves y listas de calificaciones 
#como valores, calcular la calificación más alta de cada estudiante y almacenar los resultados en un nuevo diccionario:
print(">>> EJERCICIO 18")
estudiantes_calificaciones = {'Juan': [85, 90, 95], 'María': [78, 82, 80], 'Pedro': [90, 92, 88]}
print("Diccionario original -->", estudiantes_calificaciones)

def calificacion_mas_alta(estudiante):
    nombre, calificacion = estudiante
    calificacion_maxima = max(calificacion)
    return nombre, calificacion_maxima

print("Nuevo diccionario -->", dict(map(calificacion_mas_alta,estudiantes_calificaciones.items())))

print("\n--------------------------------------\n")

# Ejercicio 19
#19. Dada una lista de números, calcular el logaritmo natural de cada número y almacenar los resultados en una lista:
print(">>> EJERCICIO 19")
lista_numeros = [1, 2, 3, 4, 5]
print("Lista original -->", lista_numeros)

def logaritmo_natural(elem):
    return round(math.log(elem),3)

print("Nueva lista -->", list(map(logaritmo_natural,lista_numeros)))

print("\n--------------------------------------\n")

# Ejercicio 20
#20. En una lista de frases, eliminar las palabras que tengan menos de 3 letras, 
#contar la cantidad de palabras en cada frase y almacenar los resultados en una lista:
print(">>> EJERCICIO 20")
lista_frases = ['Python es un lenguaje de programación.', 'Tiene una sintaxis sencilla y elegante.']
print("Lista original -->", lista_frases)



print("\n--------------------------------------\n")