'''
La función filter sigue la dinámica del map() pero devuelven los datos
de la condición marcada por la función (debe ser True o False)

'''

'''
La función reduce sigue la dinámica del map() pero devuelve un único dato. 
En este caso recibe 2 parámetros y los va sumando continuamente

'''
from functools import reduce # --> MEMORIZAR

lista_nums = list(range(1,10000))
def pares(x):
    return x%2==0

def sumar(x,y):
    return x+y

lista_filtrada = filter(pares, lista_nums)
suma_numeros = reduce(sumar,lista_filtrada)

#suma_numeros = reduce (sumar, filter(pares,lista_nums))

print(suma_numeros)

'''
Tengo una lista de objetos y quiero solo aquellas personas que tengan menos de 10.000€, le doy un % de dinero y cuanto dinero se da
    -Hay que aplicar filter, map y reduce (suelen usarse juntos)
'''