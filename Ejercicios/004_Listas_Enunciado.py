import random as rd

'''
Ejercicio 1:
Crear una lista vacía y agregar elementos.
Escribe un programa que cree una lista vacía llamada "mi_lista" y agregue los números del 1 al 5 a esta lista.
'''
print(">> EJERCICIO 1")
print()

mi_lista = list()

for indice in range (1,6):
    mi_lista.append(indice)

print("La lista es:" , mi_lista)

print("-------------------------------------------")
print()


'''
Ejercicio 2:
Acceder a elementos de una lista.
Escribe un programa que defina una lista llamada "colores" que contenga los nombres de varios colores y muestre el primer y el último elemento de la lista.
'''
print(">> EJERCICIO 2")
print()

colores = ["rojo","azul","verde","morado","amarillo"]
print("El primer color de la lista es:" , colores[0])
print("El último color de la lista es:" , colores[len(colores)-1])

print("-------------------------------------------")
print()


'''
Ejercicio 3:
Modificar elementos de una lista.
Escribe un programa que tenga una lista de números del 1 al 5 y cambie el tercer elemento de la lista por el número 10.
'''
print(">> EJERCICIO 3")
print()

numeros = [1,2,3,4,5]
print("La lista inicial es:" , numeros)
numeros[2] = 10
print("La nueva lista es:" , numeros)

print("-------------------------------------------")
print()


'''
Ejercicio 4:
Eliminar elementos de una lista.
Escribe un programa que tenga una lista de nombres de frutas y elimine el segundo elemento de la lista.
'''
print(">> EJERCICIO 4")
print()

frutas = ["pera","manzana","platano","sandia","naranja"]
print("La lista inicial es:" , frutas)
frutas.pop(1)
print("La nueva lista es:" , frutas)

print("-------------------------------------------")
print()


'''
Ejercicio 5:
Contar elementos de una lista.
Escribe un programa que cuente cuántas veces aparece la palabra "perro" en una lista dada.
'''
print(">> EJERCICIO 5")
print()

lista = ["perro", "gato"]*5
print("La lista inicial es:" , lista)
print("El número de veces que se repite 'perro' es:" , lista.count("perro"))

print("-------------------------------------------")
print()


'''
Ejercicio 6:
Crear una lista a partir de elementos ingresados por el usuario.
Escribe un programa que solicite al usuario ingresar 5 nombres y cree una lista con estos nombres.
'''
print(">> EJERCICIO 6")
print()

'''
print("Ingrese 5 nombres:")
nombres = list()

for indice in range(1,6):
    print("Nombre" , indice , ": " , end="")
    nombres.append(input())
    
print("Los nombre son:" , nombres)
'''

print("-------------------------------------------")
print()


'''
Ejercicio 7:
Concatenar dos listas.
Escribe un programa que tenga dos listas de números y las concatene para formar una sola lista.
'''
print(">> EJERCICIO 7")
print()

list1 = [1,2,3]
list2 = [4,5,6]

print("La lista 1 es:" , list1)
print("La lista 2 es:" , list2)
print("La lista final es:" , list1+list2)

print("-------------------------------------------")
print()


'''
Ejercicio 8:
Ordenar una lista alfabéticamente.
Escribe un programa que tenga una lista de nombres de países y los ordene alfabéticamente.
'''
print(">> EJERCICIO 8")
print()

paises = ["españa","francia","alemania","portugal","bélgica"]

paises.sort()
print("La lista ordenada es:" , paises)

print("-------------------------------------------")
print()


'''
Ejercicio 9:
Reemplazar elementos de una lista.
Escribe un programa que tenga una lista de números del 1 al 5 y reemplace los elementos del segundo al cuarto por el número 0.
'''
print(">> EJERCICIO 9")
print()

numeros = [1,2,3,4,5]
print("La lista inicial es:" , numeros)

for i in range(1, 4):
    numeros[i] = 0

print("La lista final es:" , numeros)

print("-------------------------------------------")
print()


'''
Ejercicio 10:
Buscar un elemento en una lista.
Escribe un programa que tenga una lista de números y verifique si el número 5 está presente en la lista.
'''
print(">> EJERCICIO 10")
print()

numeros = [1,2,3,4,5,6,7,8,9,10]
print("Lista de números:" , numeros)

if not numeros.__contains__(5) :
    print("No hay ningun 5 en la list")
else :
    print("El número de 5's es:" , numeros.count(5))

print("-------------------------------------------")
print()


'''
Ejercicio 11:
Calcular la longitud de una lista.
Escribe un programa que tenga una lista de colores y calcule cuántos elementos tiene la lista.
'''
print(">> EJERCICIO 11")
print()

colores = ["rojo","azul","verde","morado","amarillo"]
print("Lista de colores:" , colores)
print("El número de colores es:" , len(colores))

print("-------------------------------------------")
print()


'''
Ejercicio 12:
Crear una lista de números pares.
Escribe un programa que cree una lista de los primeros 5 números pares a partir de un rango.
Agrega esos números pares a una lista
'''
print(">> EJERCICIO 12")
print()

numerosPares = list()

for i in range(10,20):
    if i % 2 == 0 and len(numerosPares) < 5:
        numerosPares.append(i)
        
print("La lista es:" , numerosPares)

print("-------------------------------------------")
print()


'''
Ejercicio 13:
Sumar todos los elementos de una lista.
Escribe un programa que tenga una lista de números y sume todos sus elementos.
'''
print(">> EJERCICIO 13")
print()

numeros = [2,4,6,8,10,12,14,16,18,20]
print("La lista es:" , numeros)

sumatorio = 0
for i in numeros:
    sumatorio += i

print("La suma de sus elementos es:" , sumatorio)

print("-------------------------------------------")
print()


'''
Ejercicio 14:
Contar elementos mayores que un número dado.
Escribe un programa que tenga una lista de números y cuente cuántos elementos son mayores que 5.
'''
print(">> EJERCICIO 14")
print()

numeros = [2,4,6,8,10,12]
print("La lista es:" , numeros)

sumatorio = 0 
for i in numeros:
    if i>5:
        sumatorio +=1
        
print("El número de elementos mayores que 5 es:" , sumatorio)

print("-------------------------------------------")
print()


'''
Ejercicio 15:
Eliminar duplicados de una lista.
Escribe un programa que tenga una lista con elementos duplicados y elimine los duplicados de la lista.
'''
print(">> EJERCICIO 15")
print()

elementos = ["hola", "hola", "buenos", "hola", "hola", "buenos", "dias"]
print("La lista es:" , elementos)

for elem in elementos:
    while elementos.count(elem) != 1 :
        elementos.remove(elem)

print("La lista final eliminando duplicados es:" , elementos)

print("-------------------------------------------")
print()


'''
Ejercicio 16:
Multiplicar todos los elementos de una lista.
Escribe un programa que tenga una lista de números y multiplique todos sus elementos entre sí.
'''
print(">> EJERCICIO 16")
print()

numeros = [1,2,3,4,5]
print("La lista es:" , numeros)

resultado = 1
for num in numeros:
    resultado *= num
    
print("El resultado de multiplicar los elementos es:" , resultado)

print("-------------------------------------------")
print()


'''
Ejercicio 17:
Comprobar si una lista está vacía.
Escribe un programa que determine si una lista dada está vacía o no.
'''
print(">> EJERCICIO 17")
print()

list1 = []
list2 = [1,2,3,4,5]

if len(list1) == 0 :
    print("La lista 1 está vacía")
else:
    print("La lista 1 no está vacía")
    
if len(list2) == 0 :
    print("La lista 2 está vacía")
else:
    print("La lista 2 no está vacía")



print("-------------------------------------------")
print()


'''
Ejercicio 18:
Calcular el promedio de una lista de números.
Escribe un programa que tenga una lista de números y calcule el promedio de esos números.
'''
print(">> EJERCICIO 18")
print()

numeros = [1,2,3,4,5,6,7,8,9]
print("La lista es:" , numeros)

sumatorio = 0
for num in numeros:
    sumatorio += num

resultado = sumatorio / len(numeros)
print("El promedio es:" , resultado)

print("-------------------------------------------")
print()


'''
Ejercicio 19:
Calcular la suma de los elementos pares de una lista.
Escribe un programa que tenga una lista de números y calcule la suma de todos los elementos pares en la lista.
'''
print(">> EJERCICIO 19")
print()

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("La lista es:" , numeros)

sumatorio = 0
for num in numeros:
    if num % 2 == 0:
        sumatorio += num
        
print("La suma de los elementos pares es:" , sumatorio)

print("-------------------------------------------")
print()


'''
Ejercicio 20:
Reemplazar todos los elementos de una lista con un valor dado.
Escribe un programa que tenga una lista de números y reemplace todos sus elementos por un valor dado.
'''
print(">> EJERCICIO 20")
print()

numeros = [1,2,3,4,5,6,7,8]
print("La lista es:" , numeros)

for i in range(len(numeros)):
    numeros[i]= 9

print("La nueva lista reemplazando por 9 es:" , numeros)

print("-------------------------------------------")
print()


'''
Ejercicio 21:
Invertir una lista.
Escribe un programa que tenga una lista de números y la invierta, es decir, que el primer elemento se convierta en el último y viceversa.
'''
print(">> EJERCICIO 21")
print()

numeros = [1,2,3,4,5,6,7,8,9]
print("La lista es:" , numeros)

numerosInvertidos = []
for i in range(len(numeros)  , 0 , -1):
    numerosInvertidos.append(i)
 
print("La nueva lista inversa es:" , numerosInvertidos)
numeros.reverse()
print("La nueva lista inversa es:" , numeros)

print("-------------------------------------------")
print()


'''
Ejercicio 22:
Dividir una lista en partes iguales.
Escribe un programa que tenga una lista de números y la divida en partes iguales de longitud especificada por el usuario.
'''
print(">> EJERCICIO 22")
print()

def dividir_lista(lista, num_partes):
    longitud_sublista = len(lista) // num_partes
    partes = []
    inicio = 0
    for i in range(num_partes):
        partes.append(lista[inicio:inicio + longitud_sublista])
        inicio += longitud_sublista
    return partes

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_partes = 3
partes_resultantes = dividir_lista(mi_lista, num_partes)
print(partes_resultantes)

print("-------------------------------------------")
print()


'''
Ejercicio 23:
Ordenar una lista en orden descendente.
Escribe un programa que tenga una lista de números y la ordene en orden descendente.
'''
print(">> EJERCICIO 23")
print()

numeros = [3,6,5,8,9,2,1]
print("La lista es:" , numeros)

for i in range(len(numeros)):
    max_index = i
    for j in range(i + 1, len(numeros)):
        if numeros[j] > numeros[max_index]:
            max_index = j
    numeros[i], numeros[max_index] = numeros[max_index], numeros[i]


print("La lista ordenada descendente es:" , numeros)

numeros.sort(reverse=True)
print("La lista ordenada descendente es:" , numeros)


print("-------------------------------------------")
print()


'''
Ejercicio 24:
Unir dos listas en una sola.
Escribe un programa que tenga dos listas de números y las una en una sola lista.
'''
print(">> EJERCICIO 24")
print()

numeros1 = [1,2,3,4,5]
print("La lista1 es:" , numeros1)
numeros2 = [6,7,8,9,10]
print("La lista2 es:" , numeros2)

numerosTotal = numeros1+numeros2

print("La lista final es:" , numerosTotal)

print("-------------------------------------------")
print()


'''
Ejercicio 25:
Eliminar todos los elementos duplicados de una lista.
Escribe un programa que tenga una lista con elementos duplicados y elimine todos los duplicados, dejando solo una ocurrencia de cada elemento.
'''
print(">> EJERCICIO 25")
print()

numeros = [1,2,4,6,7,7,6,3,4,5,9,1,2,3]
print("La lista es:" , numeros)

for num in numeros:
    while numeros.count(num) > 1 :
        print("Eliminando" , num , "...")
        numeros.remove(num)
        
        
print("La lista final es:" , numeros)

print("-------------------------------------------")
print()


'''
Ejercicio 26:
Ordenar una lista de cadenas alfabéticamente sin distinción entre mayúsculas y minúsculas:

Escribe un programa que solicite al usuario ingresar una lista de palabras 
y luego ordene la lista alfabéticamente sin distinguir entre mayúsculas y minúsculas.
Además, el programa debe eliminar cualquier palabra duplicada antes de realizar la ordenación.
'''
print(">> EJERCICIO 26")
print()

palabras = ["hola", "buenos", "dias", "que", "Tal", "dias", "Estas", "hola"]
print("La lista es:" , palabras)

#ELiminamos las palabras duplicadas
for palabra in palabras :
    if palabras.count(palabra) > 1 :
        palabras.remove(palabra)
        

# Convertir todas las palabras a minúsculas para ignorar distinción de caso
palabras_minusculas = []
for palabra in palabras:
    palabras_minusculas.append(palabra.lower())
    
for i in range(len(palabras_minusculas)):
    min_index = i
    for j in range(i + 1, len(palabras_minusculas)):
        if palabras_minusculas[j] < palabras_minusculas[min_index]:
            min_index = j
    palabras_minusculas[i], palabras_minusculas[min_index] = palabras_minusculas[min_index], palabras_minusculas[i]
    

print("La lista final es:" , palabras_minusculas)


print("-------------------------------------------")
print()


'''
Ejercicio 27
Escribe un programa que genere dos listas de números aleatorios entre 1 y 20 
y luego calcule e imprima la intersección de estas dos listas,
es decir, los números que aparecen en ambas listas.
Asegúrate de que no haya duplicados en las listas generadas.
'''
print(">> EJERCICIO 27")
print()

lista1 = []
lista2 = []

l1Completa = False
l2Completa = False
#Generamos las listas aleatorias de tamaño 11
while not l1Completa and not l2Completa:
    if not l1Completa:
        numero1 = rd.randint(1,20)
        if lista1.count(numero1) < 1:
            lista1.append(numero1)
            
    if not l2Completa:    
        numero2 = rd.randint(1,20)
        if lista2.count(numero2) < 1:
            lista2.append(numero2)
            
    if len(lista1) == 11:
        l1Completa = True 
    if len(lista2) == 11:
        l2Completa = True
        
        
print("La lista 1 es:" , lista1)
print("La lista 2 es:" , lista2)

interseccion = []

for elem in lista1:
    if lista2.__contains__(elem):
        interseccion.append(elem)

print("La lista intersección es:" , interseccion)

print("-------------------------------------------")
print()


'''
Ejercicio 28
Eliminar elementos repetidos de una lista manteniendo el orden original:

Escribe un programa que reciba una lista de números y elimine los elementos 
repetidos de la lista manteniendo el orden original.
'''
print(">> EJERCICIO 28")
print()

numeros = [1,2,4,6,7,7,6,3,4,5,9,1,2,3]
print("La lista es:", numeros)

numeros_sin_repetir = []
for num in numeros:
    if num not in numeros_sin_repetir:
        numeros_sin_repetir.append(num)

print("La lista sin elementos repetidos es:", numeros_sin_repetir)



print("-------------------------------------------")
print()


'''
Ejercicio 29
Calcular la media de una lista de números:
Escribe un programa que calcule la media de una lista de números ingresada por el usuario.
'''
print(">> EJERCICIO 29")
print()

numeros = [1,2,4,6,7,7,6,3,4,5,9,1,2,3]
print("La lista es:", numeros)

sumatorio = 0
for num in numeros:
    sumatorio+=num

media = sumatorio / len(numeros)
print("La media de la lista es:", round(media,2))

media = sum(numeros) / len(numeros)
print("La media de la lista es:", round(media,2))

print("-------------------------------------------")
print()


'''
Ejercicio 30
Encontrar el elemento más grande y el más pequeño en una lista:
Escribe un programa que encuentre el elemento más grande y el más pequeño en una lista de números.
'''
print(">> EJERCICIO 30")
print()

numeros = [1,2,4,6,7,7,6,3,4,5,9,1,2,3]
print("La lista es:", numeros)

maximo = numeros[0]
minimo = numeros[0]
for num in numeros:
    if num > maximo:
        maximo = num
    if num < minimo:
        minimo = num

print("El elemento más grande de la lista es:", maximo)
print("El elemento más pequeño de la lista es:", minimo)

maximo = max(numeros)
minimo = min(numeros)
print("El elemento más grande de la lista es:", maximo)
print("El elemento más pequeño de la lista es:", minimo)



print("-------------------------------------------")
print()