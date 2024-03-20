import copy

lst =[1,2,3,4,5,["a","b","c"]]

#En ocasiones querremos copiar esa lista
lst1=lst

print(lst)
lst1[0]=100
print(lst)
print(lst1)

#Como podemos ver al modificar cualquiera de los dos, como ambos apuntan al mismo objeto, se modifican las dos
#Asique al hacer lst1=lst ambos elementos siempre serán iguales

#Por ello tenemos la funcion .copy() --> copia superficial
lst2 = lst.copy()

lst2[0]=200
print(lst)
print(lst2)

#En este caso vemos que los valores ya son diferentes

#El problema es que el .copy solo es valido si hay elementos en una lista, cuando hay una lista dentro de otra
#la función puede copiar mal, por eso usamos .deepcopy()

#Tenemos que hacer import copy
lst3 = copy.deepcopy(lst)

print("Lista:", lst)
print("Lista1:", lst1)
print("Lista2:", lst2)
print("Lista3:", lst3)