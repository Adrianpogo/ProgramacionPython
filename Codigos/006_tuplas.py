'''
Las tuplas no soportan asignación de elementos, una vez se crean no se pueden modificar

OPERACIONES CON LAS TUPLAS --> 
    - Crear tupla
    - Saber elementos de la tupla
    - Saber número de elementos de la tupla
'''

#Para definir una tupla
tupla = (1,2,3,4)

#Para imprimir una tupla
print(tupla)

#Para imprimir un elemento de una tupla
print("Elemento 2" , tupla[2])

#Contar número de elementos de la tupla
print("Numeros de 3's" , tupla.count(3))

#Para saber el tamaño de la tupla
print("Longitud de la tupla" , len(tupla))


'''
Para operar con tuplas podemos convertirlo en lista y posteriormente volver a convertirlo a tupla
'''