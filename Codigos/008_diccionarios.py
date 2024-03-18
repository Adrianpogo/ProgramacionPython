'''
Son similares a los hahmap en Java --> siguen el modelo clave-valor
Se identifican con "{}"
'''

#Para definir un diccionario
dicc = {"elem1":1, "elem2":[1,2,3] }
print(dicc)

#Para acceder a valores en concreto
print(dicc["elem2"])
print(dicc["elem2"][2]) # --> Para acceder a un valor dentro de la lista del diccionario

#Para recorrer el diccionario
for key in dicc:
    print(key)
    
#Para obtener las claves sin bucles --> devuelve un dict_keys (tipo de datos), por ello convertimos a lista
claves = list(dicc.keys()) 
print(claves)

#Para obtener los valores ocurre lo mismo
valores = list(dicc.values())
print(valores)

#Para recorrer tanto la clave con el valor
for k,v in dicc.items():
    print("Clave:" , k , "| Valor:" , v)
    
#ELiminar elementos (por su clave) --> devuelve el elemento borrado y si no existe el mensaje del parametro2 (opcional)
print(dicc.pop("elem1","Esta clave no existe"))


print(dicc.get("elem2"))
print(dicc["elem2"])