'''
La función map() permite aplicar una función a todos los elementos de un elemento dado

Recibe 2 parámetros:
    - Función --> Se escribe solo el nombre (sin los parentesis) y en su creación debe tener al menos 1 parámetro
    - Elemento a recorrer

Ejemplo: Sumar 1 a cada elemento de la lista

[1,2,3,4,5] --> [2,3,4,5,6]

--> Para imprimir un map debemos convertirlo a lista o a otro elemento antes


Se suele usar para recorrer elementos con grandes cantidades sobre los que queremos realizar una función

'''
#------------------------------------------------------------------------------------------------------------------#
print(">> EJEMPLO 1 <<\n")

def sumar1 (x):
    return x+1

lista = [1,2,3,4,5]
print("La lista inicial es:", lista)
print("La lista aplicando map es:",list(map(sumar1, lista)))

print("_______________________")

#------------------------------------------------------------------------------------------------------------------#

print("\n>> EJEMPLO 2 <<\n")
# Para este ejemplo las listas deben de ser de la misma cantidad, si no ignora el resto de elementos

def sumarList(x,y):
    return x+y

lista2 = [10,20,30,40,50]
print("La lista nueva es:", lista2)

print("La suma de listas aplicando map es:",list(map(sumarList, lista, lista2)))

print("_______________________")

#------------------------------------------------------------------------------------------------------------------#

print("\n>> EJEMPLO 3 <<\n")

lista3 = ["Hola", "que", "tal"]
print("La lista3 es:", lista)

# Para obtener la longitud de los elementos
print("La longitud de los elementos de lista3 con map es:",list(map(len,lista3)))

# Para convertir a mayúsculas cada elemento
print("La lista3 mayusculas con map es:",list(map(str.upper,lista3)))

print("_______________________")

#------------------------------------------------------------------------------------------------------------------#

print("\n>> EJEMPLO 4 <<\n")

# Sumar 1 al valor asociado a una clave
dicc=[{"persona":"Andres", "edad":30},
      {"persona":"Juan", "edad":30},
      {"persona":"Alberto", "edad":30},
      {"persona":"Raul", "edad":30}]

def sumarAño (diccionario):
    if diccionario["persona"]=="Andres":
        diccionario["edad"]+=1

    # El return no es necesario ya que los valores del diccionario se cambian por referencia
    return diccionario

# Sin el return mostrará None,None,None,None
print(list(map(sumarAño,dicc)))
# Se puede imprimir así sin el return --> print(dicc)

print("_______________________")

#------------------------------------------------------------------------------------------------------------------#

print("\n>> EJEMPLO 5 <<\n")

import time
# Permite saber el timpo que tarda en ejecutarse el código y es útil para la optimización de este

# Lista de 10 millones de elementos
lst=list(range(1,1000000000))

#Tiempos para un bucle For
inicioB = time.time()
for x in range(len(lst)):
    lst[x]+=1
finalB = time.time()
print("El tiempo de ejecución con un For es:", finalB-inicioB)

#Tiempos para un bucle For-Each
inicioB2 = time.time()
for elem in lst:
    elem+=1
finalB2 = time.time()
print("El tiempo de ejecución con un For-Each es:", finalB2-inicioB2)

#Tiempos para un Map
inicioM = time.time() 
list(map(sumar1, lst))
finalM = time.time()
print("El tiempo de ejecución con Map es:", finalM-inicioM)