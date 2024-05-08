'''
Desarrollo de Clases en Python

La clase Producto en Python está diseñada para representar productos en una máquina expendedora.
Cuenta con tres atributos principales: nombre, que es un string para el nombre del producto; 
precio, que es un float que indica el precio del producto; y cantidad, que es un integer que representa 
la cantidad disponible del producto. Los métodos de esta clase incluyen el para inicializar un producto,
modificar la función que devuelve una cadena que representa la información del producto (se pueden añadir todas las funciones que se deseen). 
Se considerará que dos Productos son iguales si su nombre es igual, indistintamente de si está escrito en mayúsculas como si está en minúsculas

Por otro lado, la clase MaquinaExpendedora maneja el conjunto de productos disponibles para la venta. 
Esta clase tiene un solo atributo: inventario de productos. Esta clase Incluye varios métodos: un constructor para inicializar
la máquina sin productos, una función para añadir un producto al inventario en una cantidad concreta, 
una función para reducir en 1 un producto en concreto y una función que imprime la lista de productos 
disponibles con su información detallada, por último, una función que permite a los usuarios comprar un 
producto realizando las comprobaciones necesarias y lógicas de una máquina de estas características.

En el main se deben hacer todas las comprobaciones necesarias, para probar todas las funciones realizadas.


Cada clase tiene que estar en un fichero diferente, así como el main.py


'''

from functools import reduce

lista_de_personas = [
    {'nombre': 'Ana', 'edad': 28, 'hobbies': ['leer']},
    {'nombre': 'Carlos', 'edad': 34, 'hobbies': ['pintar', 'escalar']},
    {'nombre': 'Diana', 'edad': 21, 'hobbies': ['nadar', 'correr', 'cocinar']},
    {'nombre': 'Elena', 'edad': 26, 'hobbies': ['viajar']},
    {'nombre': 'Fernando', 'edad': 31, 'hobbies': ['videojuegos', 'dibujo', 'guitarra', 'canto']},
    {'nombre': 'Gloria', 'edad': 23, 'hobbies': ['yoga', 'meditación']},
    {'nombre': 'Héctor', 'edad': 29, 'hobbies': ['fotografía']},
    {'nombre': 'Irene', 'edad': 35, 'hobbies': ['ciclismo', 'lectura', 'escribir']},
    {'nombre': 'Jorge', 'edad': 30, 'hobbies': ['teatro', 'cine', 'baile', 'escultura']},
    {'nombre': 'Laura', 'edad': 24, 'hobbies': ['ajedrez']}
]

'''
Los siguientes ejercicios solo se pueden realizar con map, filter y reduce. Se puede usar otras funciones pero no ningún tipo de bucle

- Dame la persona de más edad
- Dame la persona con mayor número de hobbies
- De cada una de las personas dame el hobbie con nombre más largo
- Dame todos los nombres las personas y sus edades con la siguiente estructura:
    - nombre1 , edad1 <-> nombre2 , edad3 <-> nombre3 , edad3 <-> ...
'''

# -------------------------------------------- EJERCICIO 1 ---------------------------------------------

# Obtenemos la lista de edades
lista_edades = list(map(lambda persona: persona['edad'], lista_de_personas))

# Calculamos cúal es la edad mayor con un max de la lista de edades    
edad_mayor = max(lista_edades)

# Hacemos un filtrado en la lista original devolviendo los diccionarios cuya clave edad sea igual a la edad máxima
persona_mayor = list(filter(lambda persona: persona['edad']==edad_mayor , lista_de_personas))
print("\nLa lista de personas con la edad mayor es:", persona_mayor)

# -------------------------------------------- EJERCICIO 2 ---------------------------------------------

# Obtenemos la lista de hobbies y tras ello la longitud para saber el número de hobbies de cada persona
lista_hobbies = list(map(lambda persona: persona['hobbies'], lista_de_personas))
lista_num_hobbies = list(map(lambda hobbies: len(hobbies), lista_hobbies))

# Con ayuda del max obtenemos el número máximo de hobbies de una persona
max_num_hobbies = max(lista_num_hobbies)

# Finalmente devolvemos la lista de personas con ese número de hobbies, en este caso serán 2, para ello usamos 
# un filter con el número máximo de hobbies
personas_max_hobbies = list(filter(lambda persona: len(persona['hobbies']) == max_num_hobbies , lista_de_personas))

print("\nLa lista de personas con más hobbies es:" , personas_max_hobbies)

# -------------------------------------------- EJERCICIO 3 ---------------------------------------------

# Función auxiliar para escoger la palabra más larga
def palabra_mas_larga (x,y):
    if len(x)>len(y):
        return x
    elif len(x)<len(y):
        return y
    else: return x

# Teniendo la lista de hobbies del apartado anterior y ayudandonos de la función para buscar la palabra
# más larga, devolvemos la lista de hobbies pero reducida con solo el hobbie más largo
lista_hobbie_largo = list(map(lambda hobbie: reduce(palabra_mas_larga, hobbie), lista_hobbies))

# Guardamos el nombre de las personas en una lista
lista_nombres = list(map(lambda persona: persona['nombre'], lista_de_personas))

# Hacemos un zip de la lista con nombres de las personas y los hobbies más largos, de está forma se
# creará una lista de tuplas compuestas por el nombre seguido del hobbie más largo de esa persona
# ya que se conserva el orden de la lista orginal
lista_nombre_hobbie = list(zip(lista_nombres, lista_hobbie_largo))
print("\nLa lista de los hobbies más largos de cada persona es:", lista_nombre_hobbie)



# -------------------------------------------- EJERCICIO 4 ---------------------------------------------

# Convertimos todos los elementos de la lista de edades usada anteriormente a str para evitar fallos concatenando
lista_edades_str = list(map(lambda edad: str(edad) , lista_edades))

# Hacemos un zip para crear una lista de tuplas con cada nombre y su edad
lista_nombre_edad = list(zip(lista_nombres, lista_edades_str))

# Concatenamos cada elemento de dentro de la lista para que los elementos dentro de cada elemento aparezcan 
# separados por "," de forma que tengamos ['Ana , 28' , 'Carlos , 34' ...]
lista_completa = list(map(lambda persona: reduce(lambda x,y: x+" , "+y , persona) ,lista_nombre_edad))

# El último paso es concatener cada elemento de la lista separándolos por "<->", para ello hacemos un reduce
# siguiendo el mismo procedimiento que en el paso anterior y obteniendo así una única cadena de caracteres
frase = reduce(lambda x,y: x+" <-> "+y , lista_completa)
print("\n", frase)