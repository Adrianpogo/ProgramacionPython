import random as rd
import string as str
#Podemos renombrar las librerias, en este caso en vez de hacer random. haremos rd.

'''
=======================================================================
|                                                                     |
|                         FUNCIONES STRING                            |
|                                                                     |
=======================================================================
'''
#String de todas las letras en mayúscula (lowercase lo hace en mníscula) --> ascii_letters devuelve ambas
print(str.ascii_uppercase)

#String de todos los numeros (.hexadigits = números hexadecimales)
print(str.digits)

#Formas de representar un espacio --> se convierte a lista para ver la respresentación
print(list(str.whitespace))

#Formas de representar signos de puntuación
print(str.punctuation)

#Colocar mayúsculas (primer parámetro = la frase // segundo parámetro = el separdor de palabras)
#Como separador por defecto se coge el espacio en blanco
print(str.capwords("esta es una frase"," "))


'''
=======================================================================
|                                                                     |
|                         FUNCIONES RANDOM                            |
|                                                                     |
=======================================================================
'''
#Número aleatorio entre un rango ( 0 , 1 ]
print(rd.random())

#Número aleatorio entre dos valores (ambos valores están incluidos)
print(rd.randint(1,5))

#Número aleatorio entre dos valores (el primero incluido, el segundo excluido)
#Como los rango podemos elegir de cuánto en cúanto saltamos
#Actua como los rangos
print(rd.randrange(1,10,2)) #Valores entre: 1,3,5,7,9

#Devolver un elemento aleatorio de una secuencia pasada por parámetros
lst = list(str.ascii_letters)
print(rd.choice(lst))

#Mezclar los daros de un elemento por parametros
rd.shuffle(lst)
print(lst)

#Coger una lista de elementos, los porcentajes de salir de cada uno y el número de elementos que se devuelve
print(rd.choices([1,2,3,4], [70,10,10,10], k=10))

#Valor alatorio decimal entre dos valores
print(rd.uniform(5,10))