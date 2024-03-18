'''
Un conjunto es una lista de elementos únicos, aunque los tenga no los refleja
Se identifican con "{}"
'''

varLista = [1,1,1,2,3,4,4,5,1,1,5]
varConjunto = {1,1,1,2,3,4,4,5,1,1,5}

print(varLista)
print(varConjunto)

'''
EL problema de los conjuntos es que por su código hash, puede ocurrir que el orden no sea el lógico
por lo tanto no podemos fiarnos de las posiciones tal y como ocurria con los hashmap en Java
'''

'''
OPERACIONES CON LOS CONJUNTOS -->
    - Añadir
    - Eliminar
    - Saber la longitud y el tipo
'''

#Añadir --> No se pueden añadir listas (porque estas varían)
varConjunto.add(6)
varConjunto.add("1")
varConjunto.add((1,2,3))
print(varConjunto)

#Eliminar --> Especificamos el elemento a eliminar ya que solo está una vez
varConjunto.discard(3)
print(varConjunto)

'''
Los conjuntos no se pueden concatener "conjunto1+conjunto2" , para añadir un conjunto a otro usamos .update
que añade al conjunto 1 los datos del conjunto 2. En caso de que el conjunto 2 tenga elementos que ya están
en el conjunto 1, estos se ignoran y no se añaden
'''

varConjunto2 = {6,7,8}
varConjunto.update(varConjunto2)
print(varConjunto)