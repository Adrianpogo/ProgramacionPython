"""
Ejercicio 1: Crear un diccionario que almacene los nombres de estudiantes 
y sus notas finales. 
Luego, agregar funcionalidad para cambiar la nota de un estudiante y 
mostrar la nota modificada.
"""

print("\n>> EJERCICIO 1")
print()

estudiantes = {
    "Juan": 85,
    "María": 90,
    "Pedro": 75,
    "Ana": 95
}

def cambiar_nota(estudiantes, nombre, nueva_nota):
    if nombre in estudiantes:
        estudiantes[nombre] = nueva_nota
        print(f"Nota de {nombre} modificada a {nueva_nota}")
    else:
        print("El estudiante no se encuentra en el diccionario")

cambiar_nota(estudiantes, "Pedro", 80)
print(estudiantes)

print("-------------------------------------------")
print()

"""
Ejercicio 2: Dado un diccionario con nombres de empleados y su salario,
calcular el salario medio, el salario más alto y el más bajo.
"""

print("\n>> EJERCICIO 2")
print()

empleados = {
    "Juan": 3000,
    "María": 3500,
    "Pedro": 2800,
    "Ana": 4000
}

def calcular_salarios(empleados):
    salario_medio = sum(empleados.values()) / len(empleados)
    salario_max = max(empleados.values())
    salario_min = min(empleados.values())
    return salario_medio, salario_max, salario_min

salario_medio, salario_max, salario_min = calcular_salarios(empleados)
print("Salario medio:", salario_medio)
print("Salario más alto:", salario_max)
print("Salario más bajo:", salario_min)


print("-------------------------------------------")
print()

"""
Ejercicio 3: Crear un programa que cuente la frecuencia de las
palabras de una frase dada por el usuario y almacene los resultados
en un diccionario.
"""

print("\n>> EJERCICIO 3")
print()

def contar_palabras(frase):
    palabras = frase.split()
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

frase = input("Introduce una frase: ")
resultado = contar_palabras(frase)
print(resultado)


print("-------------------------------------------")
print()

"""
Ejercicio 4: Dado un diccionario que almacena las preferencias
de color de los usuarios, actualizar el diccionario agregando un 
conjunto de usuarios que prefieren el mismo color.
"""

print("\n>> EJERCICIO 4")
print()

preferencias = {
    "Juan": "azul",
    "María": "verde",
    "Pedro": "rojo",
}

nuevos_usuarios = {
    "Ana": "azul",
    "Luis": "verde",
    "Eva": "rojo"
}

preferencias.update(nuevos_usuarios)
print(preferencias)


print("-------------------------------------------")
print()

"""
Ejercicio 5: Crear un programa que utilice un diccionario para 
mapear nombres de productos y sus precios. Luego, convertir este 
diccionario en una lista de tuplas, donde cada tupla contenga el 
nombre del producto y su precio.
"""

print("\n>> EJERCICIO 5")
print()

productos_precios = {
    "Manzanas": 2.5,
    "Plátanos": 1.8,
    "Naranjas": 3.0
}

lista_productos_precios = list(productos_precios.items())
print(lista_productos_precios)


print("-------------------------------------------")
print()

"""
Ejercicio 6: Crear un diccionario que almacene como clave el
nombre de un país y como valor un set de ciudades de ese país.
Añadir después una nueva ciudad a uno de los países y mostrar 
el diccionario actualizado.
"""

print("\n>> EJERCICIO 6")
print()

paises_ciudades = {
    "España": {"Madrid", "Barcelona", "Valencia"},
    "Francia": {"París", "Marsella", "Lyon"}
}

paises_ciudades["España"].add("Sevilla")
print(paises_ciudades)


print("-------------------------------------------")
print()

"""
Ejercicio 7: Dado un diccionario de productos y precios,
escribir un programa que convierta los precios a otra moneda
(por ejemplo, de euros a dólares) utilizando un tipo de cambio 
fijo, y guarde los resultados en un nuevo diccionario.
"""

print("\n>> EJERCICIO 7")
print()

def convertir_precios(diccionario_precios, tipo_cambio):
    nuevos_precios = {}
    for producto, precio in diccionario_precios.items():
        nuevos_precios[producto] = precio * tipo_cambio
    return nuevos_precios

productos_precios_euros = {
    "Manzanas": 2.5,
    "Plátanos": 1.8,
    "Naranjas": 3.0
}

tipo_cambio = 1.1  # 1 euro = 1.1 dólares
productos_precios_dolares = convertir_precios(productos_precios_euros, tipo_cambio)
print(productos_precios_dolares)


print("-------------------------------------------")
print()

"""
Ejercicio 8: Implementar un sistema de votación donde 
se almacenen los votos de diferentes candidatos en un 
diccionario. Luego, contar el total de votos y determinar el ganador.
"""

print("\n>> EJERCICIO 8")
print()

votos = {
    "Candidato A": 150,
    "Candidato B": 100,
    "Candidato C": 200
}

total_votos = sum(votos.values())
ganador = max(votos, key=votos.get)
print("Total de votos:", total_votos)
print("El ganador es:", ganador)


print("-------------------------------------------")
print()

"""
Ejercicio 9: Crear un diccionario que almacene números de teléfono
(como valores) asociados a nombres de personas (como claves).
Implementar una función que, dado el diccionario y un nombre,
devuelva el número de teléfono asociado o un mensaje indicando que no se encontró.
"""

print("\n>> EJERCICIO 9")
print()

telefonos = {
    "Juan": "123456789",
    "María": "987654321",
    "Pedro": "654321987"
}

def buscar_telefono(diccionario, nombre):
    if nombre in diccionario:
        return diccionario[nombre]
    else:
        return "No se encontró el nombre en la lista"

print(buscar_telefono(telefonos, "Juan"))
print(buscar_telefono(telefonos, "Luis"))

print("-------------------------------------------")
print()

"""
Ejercicio 10: Utilizar un diccionario para almacenar 
una lista de tuplas que representen artículos y sus cantidades 
en un inventario. Después, escribir una función que actualice 
la cantidad de un artículo específico.
"""

print("\n>> EJERCICIO 10")
print()

inventario = {
    "Manzanas": 10,
    "Plátanos": 15,
    "Naranjas": 20
}

def actualizar_cantidad(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        print("El producto no está en el inventario")

actualizar_cantidad(inventario, "Manzanas", 5)
print(inventario)

print("-------------------------------------------")
print()

"""
Ejercicio 11: Dado un diccionario que mapea los nombres de 
varios productos a sus precios por unidad, escribir un programa 
que invierta este diccionario, mapeando los precios a una 
lista de productos con ese precio.
"""

print("\n>> EJERCICIO 11")
print()

productos_precios = {
    "Manzanas": 2.5,
    "Plátanos": 1.8,
    "Naranjas": 3.0
}

precios_productos = {}
for producto, precio in productos_precios.items():
    if precio in precios_productos:
        precios_productos[precio].append(producto)
    else:
        precios_productos[precio] = [producto]

print(precios_productos)


print("-------------------------------------------")
print()

"""
Ejercicio 12: Crear un diccionario que almacene el nombre 
de estudiantes y una lista de sus calificaciones. 
Escribir un programa que calcule la media de calificaciones 
de cada estudiante y almacene el resultado en un nuevo diccionario.
"""

print("\n>> EJERCICIO 12")
print()

calificaciones_estudiantes = {
    "Juan": [85, 90, 80],
    "María": [90, 95, 88],
    "Pedro": [75, 80, 70],
    "Ana": [95, 98, 92]
}

def calcular_media(calificaciones):
    return sum(calificaciones) / len(calificaciones)

medias_calificaciones = {}
for estudiante, calificaciones in calificaciones_estudiantes.items():
    medias_calificaciones[estudiante] = calcular_media(calificaciones)

print(medias_calificaciones)


print("-------------------------------------------")
print()

"""
Ejercicio 13: Implementar un programa que almacene en un 
diccionario los votos de tres colores diferentes 
(por ejemplo, "rojo", "azul", "verde") dados por usuarios. 
El programa debe incrementar el conteo de votos cada vez que 
un color es votado y finalmente mostrar los resultados.
"""

print("\n>> EJERCICIO 13")
print()

votos_colores = {
    "Rojo": 0,
    "Azul": 0,
    "Verde": 0
}

while True:
    voto = input("Vota por un color (Rojo/Azul/Verde) o escribe 'fin' para terminar: ")
    if voto.lower() == "fin":
        break
    elif voto.capitalize() in votos_colores:
        votos_colores[voto.capitalize()] += 1
    else:
        print("Color no válido")

print(votos_colores)

print("-------------------------------------------")
print()

"""
Ejercicio 14: Dado un diccionario con nombres de personas como
claves y su año de nacimiento como valores, escribir un programa 
que calcule las edades de las personas y almacene los resultados 
en otro diccionario.
"""

print("\n>> EJERCICIO 14")
print()

from datetime import datetime

personas_nacimiento = {
    "Juan": 1990,
    "María": 1985,
    "Pedro": 1995,
    "Ana": 1980
}

anio_actual = datetime.now().year
edades = {nombre: anio_actual - nacimiento for nombre, nacimiento in personas_nacimiento.items()}
print(edades)

print("-------------------------------------------")
print()

"""
Ejercicio 15: Crear un programa que almacene las asignaturas de 
un curso (por ejemplo, matemáticas, física, química) y los estudiantes 
inscritos en ellas. Luego, permitir al usuario introducir el nombre 
de una asignatura y mostrar todos los estudiantes inscritos en ella.
"""

print("\n>> EJERCICIO 15")
print()

asignaturas_estudiantes = {
    "Matemáticas": ["Juan", "María", "Pedro"],
    "Física": ["María", "Pedro", "Ana"],
    "Química": ["Juan", "Pedro", "Ana"]
}

asignatura = input("Introduce una asignatura: ")
if asignatura in asignaturas_estudiantes:
    print("Estudiantes inscritos en", asignatura + ":", asignaturas_estudiantes[asignatura])
else:
    print("La asignatura no se encuentra en el registro")

print("-------------------------------------------")
print()

"""
Ejercicio 16: Desarrollar un programa que modele un sistema de reservas
para un hotel. El sistema debe permitir agregar y eliminar reservas. 
Cada reserva debe contener el nombre del huésped, la fecha de check-in y
check-out, y el número de habitación. Utilizar un diccionario donde 
cada clave sea el número de habitación y el valor sea otro diccionario
con los detalles de la reserva.
"""

print("\n>> EJERCICIO 16")
print()

reservas_hotel = {}

def agregar_reserva(reservas, habitacion, nombre, check_in, check_out):
    reservas[habitacion] = {
        "Nombre": nombre,
        "Check-in": check_in,
        "Check-out": check_out
    }

def eliminar_reserva(reservas, habitacion):
    if habitacion in reservas:
        del reservas[habitacion]
        print("Reserva eliminada correctamente")
    else:
        print("La habitación no tiene reserva")

# Agregar reservas de ejemplo
agregar_reserva(reservas_hotel, 101, "Juan", "2024-04-10", "2024-04-15")
agregar_reserva(reservas_hotel, 202, "María", "2024-04-12", "2024-04-18")

print("Reservas actuales:", reservas_hotel)
eliminar_reserva(reservas_hotel, 101)
print("Reservas actualizadas:", reservas_hotel)

print("-------------------------------------------")
print()

"""
Ejercicio 17: Implementar un sistema de votación por categorías, 
donde cada votante puede votar por un candidato en múltiples categorías
(por ejemplo, Mejor Director, Mejor Película). Almacenar los votos en 
un diccionario compuesto, donde las claves sean las categorías y los 
valores sean diccionarios de candidatos y la cantidad de votos recibidos.
El programa debe permitir añadir votos y determinar los ganadores por categoría.
"""

print("\n>> EJERCICIO 17")
print()

votos_categorias = {
    "Mejor Director": {"Juan": 5, "María": 8, "Pedro": 3},
    "Mejor Película": {"Juan": 7, "María": 6, "Pedro": 4}
}

def agregar_voto(votos, categoria, candidato):
    if categoria in votos:
        if candidato in votos[categoria]:
            votos[categoria][candidato] += 1
        else:
            votos[categoria][candidato] = 1
    else:
        votos[categoria] = {candidato: 1}

def determinar_ganador(votos, categoria):
    ganador = max(votos[categoria], key=votos[categoria].get)
    return ganador

# Agregar votos de ejemplo
agregar_voto(votos_categorias, "Mejor Director", "Pedro")
agregar_voto(votos_categorias, "Mejor Director", "María")
agregar_voto(votos_categorias, "Mejor Película", "Juan")
agregar_voto(votos_categorias, "Mejor Película", "María")

print("Ganador Mejor Director:", determinar_ganador(votos_categorias, "Mejor Director"))
print("Ganador Mejor Película:", determinar_ganador(votos_categorias, "Mejor Película"))

print("-------------------------------------------")
print()

"""
Ejercicio 18: Crear un programa para gestionar el inventario de una tienda. 
El inventario debe almacenar productos y sus cantidades. Implementar funciones 
para añadir productos, actualizar cantidades y mostrar el inventario actual. 
Además, implementar una búsqueda de productos por nombre.
"""

print("\n>> EJERCICIO 18")
print()

inventario_tienda = {}

def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
    else:
        inventario[producto] = cantidad

def actualizar_cantidad_producto(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] = cantidad
    else:
        print("El producto no está en el inventario")

def mostrar_inventario(inventario):
    print("Inventario actual:")
    for producto, cantidad in inventario.items():
        print(producto + ":", cantidad)

# Ejemplo de uso
agregar_producto(inventario_tienda, "Manzanas", 10)
agregar_producto(inventario_tienda, "Plátanos", 15)
agregar_producto(inventario_tienda, "Naranjas", 20)
actualizar_cantidad_producto(inventario_tienda, "Manzanas", 15)
mostrar_inventario(inventario_tienda)

print("-------------------------------------------")
print()

"""
Ejercicio 19: Desarrollar un programa que simule un sistema de 
recomendación de películas. Usar un diccionario para almacenar 
géneros de películas como claves y listas de películas como valores.
Implementar una función que, dado un género, muestre las películas 
disponibles en ese género.
"""

print("\n>> EJERCICIO 19")
print()

recomendaciones_peliculas = {
    "COMEDIA": ["La La Land", "The Grand Budapest Hotel", "Superbad"],
    "DRAMA": ["Forrest Gump", "The Shawshank Redemption", "The Godfather"],
    "ACCION": ["The Dark Knight", "Inception", "Mad Max: Fury Road"]
}

def mostrar_peliculas_por_genero(diccionario, genero):
    if genero in diccionario:
        print("Películas en", genero + ":")
        for pelicula in diccionario[genero]:
            print("-", pelicula)
    else:
        print("No hay películas en ese género")

print("Generos: Accion | Drama | Comedia\n")
genero = input("Introduce un género para ver las películas disponibles: ").upper()
mostrar_peliculas_por_genero(recomendaciones_peliculas, genero)

print("-------------------------------------------")
print()