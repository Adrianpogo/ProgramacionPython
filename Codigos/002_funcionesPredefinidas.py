# FUNCION ENUMERATE()
var1 = "hola buenos dias"

for indice, letra in enumerate(var1, start=1):
    print("La letra es:" , letra , "y su inidice es:" , indice)
    
print(list(enumerate(var1, start=1)))