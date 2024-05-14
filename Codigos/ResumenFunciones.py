'''
-----------------------------------------------------------------------------------------------------------------
                                                FUNCIONES STRING
-----------------------------------------------------------------------------------------------------------------
'''
mensaje = "Hola Mundo"


# .find --> Buscar una sub-cadena en una cadena de caracteres, devuelve el índice de inicio de esta
print(mensaje.find("Mundo")) # --> imprime 5 || En caso de no estar presente devuelve -1

# .index --> Devuelve el índice de una substring o carácter dentro de la string (si se encuentra). 
#            Si no se encuentra la substring o el carácter, genera una excepción.
print(mensaje.index("Mundo")) # --> imprime 5 || En caso de no estar sale del programa con fallo

# .lower | .upper | .capitalize --> Para convertir el formato de un texto a minúsculas o mayúsculas
print(mensaje.lower()) # --> Imprime "hola mundo"
print(mensaje.upper()) # --> Imprime "HOLA MUNDO"
print(mensaje.capitalize()) # --> Imprime "Hola mundo"


# .count --> Cuenta el número de veces que aparece un elemento 
#            Permite también dos parámetros opcionales que indican donde empezar y acabar de buscar.
print(mensaje.count("a")) # --> Imprime 1
print(mensaje.count("x")) # --> Imprime 0

# .endswith | .startswith --> Devuelve un booleano si la lista comienza o acaba con el elemento del parámetro
#                             Tiene dos parametros adicionales que son el inicio y el fin del rango de comprobacion
print(mensaje.endswith("o"))
print(mensaje.endswith("Mundo"))

# .isalnum --> Devuelve True si la cadena esta formada únicamente por caracteres alfanuméricos, 
#              False de lo contrario. Caracteres como @ o & no son alfanumericos.
#              Podemos comprobar tambien si es solo texto, digitos, etc
s = "correo@dominio.com"
print(s.isalnum()) # --> Imprime false
print(mensaje.isalnum()) # --> Imprime True

# .replace --> Reemplaza los elementos que coincidan con el primer parámetro con el elemento del segundo
print(mensaje.replace("l", "pizza")) # --> Imprime Hopizzaa Mundo

# .join --> Devuelve la primera cadena unida a cada uno de los elementos de la lista que se le pasa como parámetro.
s = " y ".join(["1", "2", "3"])
print(s) # --> Imprime "1 y 2 y 3"
print(type(s))
# .removeprefix() | .removesuffix() --> Devuelve la cadena sin el prefijo o sufijo definido, si no lo encuentra
#                                       devuelve una copia de la cadena tal cual estaba
mensaje="-Hola mundo-"
print(mensaje.removeprefix("a")) # --> Imprime "-Hola Mundo-"
print(mensaje.removeprefix("-")) # --> Imprime "Hola Mundo-"
print(mensaje.removesuffix("-").removeprefix("-")) # --> "Hola Mundo"

#.split() --> divide una cadena en subcadenas y las devuelve almacenadas en una lista. La división es realizada de acuerdo 
#             a el primer parámetro, y el segundo parámetro indica el número máximo de divisiones a realizar.
s = "Python,Java,C" 
print(s.split(",")) # --> Imprime ['Python', 'Java', 'C']
print(s.split(",",1)) # --> Imprime ['Python', 'Java,C']



'''
-----------------------------------------------------------------------------------------------------------------
                                                FUNCIONES LISTAS
-----------------------------------------------------------------------------------------------------------------
'''
# .append --> Añade un elemento al final de la lista
l = [1, 2]
l.append(3)
print(l) #[1, 2, 3]

# .extend --> Permite añadir una lista a la lista inicial
l = [1, 2]
l.extend([3, 4])
print(l) #[1, 2, 3, 4]
print(l) #[1, 2, 3, 4]

# .insert --> Añade un elemento en una posición o índice determinado
l = [1, 3]
l.insert(1, 2)
print(l) #[1, 2, 3]

# .remove --> Recibe como argumento un objeto y lo borra de la lista
l = [1, 2, 3]
l.remove(3)
print(l) #[1, 2]

# .pop --> Elimina por defecto el último elemento de la lista, pero si se pasa como parámetro un índice permite 
#          borrar el elemento en ese indice
l = [1, 2, 3]
l.pop(1)
print(l) #[1, 2]

# .reverse --> Inverte el órden de la lista
l = [3, 1, 2]
l.sort()
print(l) #[1, 2, 3]
l.sort(reverse=True)
print(l) #[3, 2, 1]

# .sort --> Ordena los elementos de menos a mayor por defecto. Permite ordenar de mayor a menor si se pasa como parámetro reverse=True
l = ["Periphery", "Intervals", "Monuments"]
print(l.index("Intervals"))

# .index --> Recibe como parámetro un objeto y devuelve el índice de su primera aparición. También permite introducir 
#            un parámetro opcional que representa el índice desde el que comenzar la búsqueda del objeto.
l = [1, 1, 1, 1, 2, 1, 4, 5]
print(l.index(1, 4)) #5



'''
-----------------------------------------------------------------------------------------------------------------
                                                FUNCIONES DICCIONARIOS
-----------------------------------------------------------------------------------------------------------------
'''
# .clear --> elimina todo el contenido del diccionario.
d = {'a': 1, 'b': 2}
d.clear()
print(d) #{}

# .get --> permite consultar el value para un key determinado. El segundo parámetro es opcional, y en el caso de 
#          proporcionarlo es el valor a devolver si no se encuentra la key.
d = {'a': 1, 'b': 2}
print(d.get('a')) #1
print(d.get('z', 'No encontrado')) #No encontrado

# .items --> devuelve una lista con los keys y values del diccionario. Si se convierte en list se puede indexar como si de una 
#            lista normal se tratase, siendo los primeros elementos las key y los segundos los value.
d = {'a': 1, 'b': 2}
it = d.items()
print(it)             #dict_items([('a', 1), ('b', 2)])
print(list(it))       #[('a', 1), ('b', 2)]
print(list(it)[0][0]) #a

# .keys --> devuelve una lista con todas las keys del diccionario.
d = {'a': 1, 'b': 2}
k = d.keys()
print(k)       #dict_keys(['a', 'b'])
print(list(k)) #['a', 'b']

# .values --> devuelve una lista con todos los values o valores del diccionario.
d = {'a': 1, 'b': 2}
print(list(d.values())) #[1, 2]

# .pop --> busca y elimina la key que se pasa como parámetro y devuelve su valor asociado. se puede pasar un segundo parámetro que 
#          es el valor a devolver si la key no se ha encontrado.  
d = {'a': 1, 'b': 2}
d.pop('a')
print(d) #{'b': 2}
d.pop('c', -1)
print(d) #{'a': 1, 'b': 2}

# .popitem --> elimina de manera aleatoria un elemento del diccionario.
d = {'a': 1, 'b': 2}
d.popitem()
print(d) #{'a': 1}

# .update --> tiene como entrada otro diccionario. Los value son actualizados y si alguna key del nuevo diccionario no esta, es añadida.
d1 = {'a': 1, 'b': 2}
d2 = {'a': 0, 'd': 400}
d1.update(d2)
print(d1) #{'a': 0, 'b': 2, 'd': 400}

'''
-----------------------------------------------------------------------------------------------------------------
                                                FUNCIONES CONJUNTOS
-----------------------------------------------------------------------------------------------------------------
'''



'''
-----------------------------------------------------------------------------------------------------------------
                                                FUNCIONES TUPLAS
-----------------------------------------------------------------------------------------------------------------
'''





'''
-----------------------------------------------------------------------------------------------------------------
                                            FUNCIONES INCORPORADAS
-----------------------------------------------------------------------------------------------------------------
'''