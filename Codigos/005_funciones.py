'''
Las funciones en python son siempre públicas no como el Java

La sintaxis es -->

        def nombreFuncion(parametros) :
            print("Hola")
            return "Esto es lo que devuelve"
    
Las funciones en python siempre devuelven algo, en caso de no devolver nada mostrará None por pantalla
Como en Python los parametros no necesitan especificacion del tipo podemos ayudarnos escribiendo:
        - strParam
        -intParam
        -lstParam
        ...
    
Podemos hacer sobrecarga de funciones, es decir, escribir dos funciones iguales pero con número 
diferente de parámetros, y lo que hará la función al llamarla es adaptarse y seleccionar la que
sea equivalente al número de parámetros que se le pasa.

Las funciones pueden hacer múltiples returns

        def multiplesReturns():
            return 1,2,3,4
            
Esto se almacena en forma de tupla (no son modificables) --> (1, 2, 3, 4)
Pero tambien podemos almacenarlos en diferentes variables

        var1, var2, var3, var4 = multiplesReturns()
        
Si queremos ignorar el dato en una posición usamos "_"

        var1, var2, var3, _ = multiplesReturns()
        
        
FUNCIONES RECURSIVAS:

        --> No recursiva
        def fibonacci(n):
            f=[0,1]
            r=0
            for x in range(0, n-1):
                r=f[x]+f[x+1]
                f.append(r)
            return f
        
        --> Recursiva  
        def fibonacciR (n):
            if n==0:
                return 0
            if n==1:
                return 1
            else:
                return fibonacciR(n-1) + fibonacciR(n-2)
        


def suma(*args) --> cuando no sabemos el numero de parametros que vamos a recibir, se recibe como una lista con los parametros              


'''
