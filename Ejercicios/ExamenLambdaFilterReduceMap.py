from functools import reduce

'''
Escribe una función calcular_promedio_palabras que tome una lista de frases como 
entrada y devuelva el promedio de la longitud de las palabras en esas frases. 

    -El promedio debe redondearse a 2 decimales
    - Puedes usar todas las fucniones auxiliares que quieras
    - Se deben ignorar aquellas palabras de 2 o menos caracteres
    - Las palabras se separan por " "
    - Los signos que queden junto a las palabras se considerarán parte de la palabra

frases=["Hola, ¿cómo estas?",
        "Me gusta programar en Python",
        "Python es genial"]

'''

def calcular_promedio_palabras(frases):
    # Obtener lista de palabras
    lista_palabras = map(lambda x: x.split(), frases)
    # Reducir  una sola lista
    palabras = reduce(lambda x, y: x + y, lista_palabras)
    # Eliminar las palabras de longitud menor a 2
    palabras_filtradas = list(filter(lambda x: len(x) > 2, palabras))
    # Obtener una lista de longitudes
    longitudes = map(lambda x: len(x), palabras_filtradas)
    # Sumar las longitudes
    promedio = reduce(lambda x, y: x + y, longitudes) / len(palabras_filtradas)
    
    return round(promedio, 2)

frases = [
    "Hola, ¿cómo estas?",
    "Me gusta programar en Python",
    "Python es genial"
]

print(calcular_promedio_palabras(frases))


