'''
============================================================================================================================================
|                                                                                                                                          |
|                                                          LISTAS EN PYTHON                                                                |
|                                                                                                                                          |
============================================================================================================================================
'''

#Formas de declarar una lista vacia
varLista = []
varLista1 = list() #Convierte el elemento de parámetros a una lista

#Formas de declarar lista con valores
varLista = [5,6,7]
varLista1 = list([1,2,3])

#Para añadir elementos a una lista (se agregan al final de la lista)
varLista.append(8)
varLista.append(9)
varLista.append(varLista1) #Se pueden añadir cualquier elemento pero no queremos que pase esto
varLista.append(9)

#Para saber en que posición esta un valor
print("El número 9 aparece", varLista.count(9) , "veces")

#Para saber la posición de la primera coincidencia de una valor
print("Posición del 9:" , varLista.index(9))

#Para eliminar un elemento por valor (elmina la primera coincidencia de se elemento)
varLista.remove(9)

#Para eliminar un elemento por posición
varLista.pop(0)

#Imprimir una lista
print(varLista)
print(varLista1)

#En las listas si hacemos un parseo a str() el tipo del elemento seguirá siendo <class 'list'>    
#En Python podemos usar indices negativos (mismo número de posiciones que positivas)  

#La posición -2 es equivalente a la penúltima (9)
print(varLista[-2])


'''
.                                                    Rangos y Listas
========================================================================================================================
'''
#Para visulizar desde la posición 1 (incluida) hasta la 4 (sin incluir) --> [1 , 4)
print(varLista[1:4])
#Podemos establecer un tercer valor para ver cuanto saltamos
print(varLista[1:4:2])

'''
.                                                    LISTAS & LISTAS
========================================================================================================================
'''
#Accedemos a la posición de la lista en la lista y tras ello a la posición de esa lista
print(varLista[3][2])

#Podemos hacer operaciones como * (multiplica para que aparezcan esas veces en la lista)
#Podemos hacer operaciones como + (se concatenan los elementos de las listas)



'''
.                                                    EJERCICIO PRUEBA
========================================================================================================================
'''

#Eliminar los 1's repetidos de la lista usando .count y .remove
lst = [1,1,1,2,6,4,87]

while lst.count(1) !=1 :
    lst.remove(1)
    
print(lst)