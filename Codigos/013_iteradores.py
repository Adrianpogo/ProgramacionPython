'''
    iter([ , , ,]) --> devuelve un elemento que permite recorrer algo

    En los for por ejemplo, se convierten los objetos internamente para poder recorrerlos

    Funciones:
        - next() --> pedir el siguiente elemento
        - hasNext() --> para saber si tiene siguiente elemento (Solo en Java)

    yield --> sustituye al return
    Su función principal es guardar, una vez salimos desde una función con un yield,
    cuando volvemos a esta, se retoma desde donde se ha salido antes.

    Para calcular el siguiente dato de una secuencia determinada, en lugar de calcular todos los anteriores


    Hay funciones concretas que devuelven un iterador o un yield

'''

def bucle ():
    i=0
    while i != 10:
        yield "Hola" + str(i)
        i +=1

'''
EJECUCIÓN -->
    - Hola0
    - Hola1
    - Hola2
    - ...

    Devuelve un objeto, tenemos que recorrer el siguiente elemento

'''

print(next(bucle())) # --> Devuelve Hola0
print(next(bucle())) # --> Devuelve Hola0

# Hay que almacenarlo en un objeto
iterador = bucle()
print(next(iterador)) # --> Devuelve Hola0
print(next(iterador)) # --> Devuelve Hola1

# Devolver todos los elementos del iterador (comienza desde el siguiente, en este caso 2)
for item in iterador:
    print(item)

'''
Una vez se vacia el iterador ya no se usa

for item in iterador:
    print(item)

Podemos solucionarlo e imprimirlo dos veces usando la función en lugar del objeto

'''

# Dará una excepción ya que se piden números de más
# while True:
#    print(next(iterador))

# Para usarlo podemos:
while True:
    try:
        print(next(iterador))
    except StopIteration:
        print("Ya no hay elementos")
        break


lst =[1,2,3,4,5,6,7]
print(iter(lst))