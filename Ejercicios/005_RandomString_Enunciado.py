import random
import string

"""
Enunciado:
Crea un programa en Python que tome una lista de palabras y mezcle aleatoriamente 
los caracteres de cada palabra,
excepto el primero y el último carácter. Por ejemplo, la palabra "Python" podría 
transformarse en "Pytnoh" o "Pyhotn",
mientras que "Hola" podría ser "Hloa" o "Halo".

Requisitos:
- La lista de palabras debe estar predefinida en el programa con al menos 5 palabras distintas.
- Utiliza los módulos 'random' y 'string' para realizar las mezclas.
- Asegúrate de que el primer y el último carácter de cada palabra permanezcan en su lugar.
"""
def mezclar_palabras(lista_palabras):
    palabras_mezcladas = []
    for palabra in lista_palabras:
        if len(palabra) > 2:  # asegurarse de que la palabra tenga al menos 3 caracteres
            inicio = palabra[0]
            final = palabra[-1]
            caracteres_intermedios = list(palabra[1:-1])
            random.shuffle(caracteres_intermedios)
            palabra_mezclada = ''.join([inicio] + caracteres_intermedios + [final])
            palabras_mezcladas.append(palabra_mezclada)
        else:
            palabras_mezcladas.append(palabra)  # si la palabra tiene menos de 3 caracteres, no se mezcla
    return palabras_mezcladas

# Lista de palabras predefinida
lista_palabras = ["Python", "Hola", "Programación", "Algoritmo", "Computadora"]

# Mezclar las palabras
palabras_mezcladas = mezclar_palabras(lista_palabras)
print("Palabras originales:", lista_palabras)
print("Palabras mezcladas:", palabras_mezcladas)

print("-------------------------------------------")
print()

"""
Enunciado:
Crea un programa en Python que simule el lanzamiento de un dado. 
El usuario debe poder especificar el número de caras del dado (por ejemplo, 
6 para un dado tradicional, 20 para un dado de rol, etc.). 
Después de especificar el número de caras, el programa debe generar y mostrar un resultado aleatorio
entre 1 y el número de caras del dado.

Requisitos:
- Pide al usuario que introduzca el número de caras del dado.
- Utiliza el módulo 'random' para generar el resultado aleatorio.
- Asegúrate de validar que el número de caras es un número válido mayor que 1.

"""
def lanzar_dado(numero_caras):
    return random.randint(1, numero_caras)

try:
    numero_caras = int(input("Ingrese el número de caras del dado: "))
    if numero_caras < 2:
        raise ValueError("El número de caras debe ser mayor que 1.")
    resultado = lanzar_dado(numero_caras)
    print("El resultado del lanzamiento es:", resultado)
except ValueError as e:
    print("Error:", e)

print("-------------------------------------------")
print()

"""
Enunciado:
Crea un programa en Python que genere un número aleatorio entre 1 y 10 y permita al usuario adivinarlo.
El programa debe indicar si el intento del usuario es demasiado alto, demasiado bajo, 
o correcto. Después de adivinar correctamente, el programa debe preguntar al usuario si 
quiere jugar de nuevo.

Requisitos:
- Utiliza el módulo 'random' para generar el número aleatorio.
- El programa debe seguir ejecutándose hasta que el usuario decida no jugar más.
- Asegúrate de capturar y manejar los errores, como entradas no numéricas.

"""
def jugar_adivina_numero():
    numero_secreto = random.randint(1, 10)
    while True:
        try:
            intento = int(input("Adivina el número (entre 1 y 10): "))
            if intento < 1 or intento > 10:
                print("El número debe estar entre 1 y 10.")
                continue
            if intento == numero_secreto:
                print("¡Correcto! El número era", numero_secreto)
                break
            elif intento < numero_secreto:
                print("Demasiado bajo.")
            else:
                print("Demasiado alto.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

jugar_adivina_numero()

print("-------------------------------------------")
print()

"""
Enunciado:
Crea un programa en Python que simule un sorteo. Dada una lista de nombres de participantes,
el programa debe seleccionar un ganador al azar y luego removerlo de la lista para evitar
que sea seleccionado nuevamente. Repite el proceso para seleccionar un segundo y tercer ganador,
asegurándote de que no se repitan los ganadores.

Requisitos:
- Utiliza una lista predefinida de nombres de participantes.
- Utiliza el módulo 'random' para seleccionar los ganadores.
- Asegúrate de que cada ganador sea único y muestre los nombres de los ganadores al final.

"""

participantes = ["Alice", "Bob", "Charlie", "David", "Eve"]

ganadores = []

while len(ganadores) < 3:
    ganador = random.choice(participantes)
    ganadores.append(ganador)
    participantes.remove(ganador)

print("Los ganadores son:", ganadores)

print("-------------------------------------------")
print()

"""
Enunciado:
Crea un programa en Python que genere nombres de usuario aleatorios para 
una lista de nombres de personas. El nombre de usuario debe ser una 
combinación de una cadena aleatoria de tres letras (pueden ser mayúsculas o minúsculas)
seguido de un número aleatorio entre 100 y 999.

Requisitos:
- Utiliza una lista predefinida de nombres completos de personas.
- Utiliza los módulos 'random' y 'string' para generar las partes del nombre de usuario.
- Genera un nombre de usuario para cada persona en la lista

"""

def generar_nombre_usuario(nombre):
    letras_aleatorias = ''.join(random.choices(string.ascii_letters, k=3))
    numero_aleatorio = random.randint(100, 999)
    return letras_aleatorias + str(numero_aleatorio)

nombres = ["Alice", "Bob", "Charlie", "David", "Eve"]

nombres_usuarios = {nombre: generar_nombre_usuario(nombre) for nombre in nombres}

for nombre, usuario in nombres_usuarios.items():
    print(f"{nombre}: {usuario}")

print("-------------------------------------------")
print()