'''
Queremos ver una lista de forma recursiva, cada vez que entremos en una estructura de almacenamiento 
deberemos dejar más espacios para así ver el árbol que genera la representación gráfica de una forma visual. 
Además, queremos dar más información visual:

• Si estoy dentro de una lista usaremos el siguiente separador ->
• Si estoy dentro de un diccionario usaremos el siguiente separador.>
• Si estoy dentro de una tupla usaremos el siguiente separador _>
• Si estoy dentro de un Set usaremos el siguiente separador =>


l = [1,2,3,(1,2,3),4,5,6,[1,{"key1":1,"key2":2,"key3":{"Alumno1","Alumno2",True}},{1,2,3}]]

La función se tiene que llamar de la siguiente forma: verListaRecursivaConTipoDatos(l,0,type(l))
asi que sus parametros son la estructura, la profundidada y el tipo de la estructura

RESULTADO:

0: -> 1
1: -> 2
2: -> 3
3: -> <class 'tuple'>
    0: _> 1
    1: _> 2
    2: _> 3
4: -> 4
5: -> 5
6: -> 6
7: -> <class 'list'>
    0: -> 1
    1: -> <class 'dict'>
        0: .> key1 --> 1
        1: .> key2 --> 2
        2: .> key3 --> <class 'set'>
            0: => True
            1: => Alumno1
            2: => Alumno2
    2: -> <class 'set'>
        0: => 1
        1: => 2
        2: => 3


'''

l = [1,2,3,(1,2,3),4,5,6,[1,{"key1":1,"key2":2,"key3":{"Alumno1","Alumno2",True}},{1,2,3}]]
print(type(l))

def verListaRecursivaConTipoDatos(elemento, profundidad, tipoElemento):
    return
    

verListaRecursivaConTipoDatos(l, 0, type(l))