''' 
    TIPOS DE DATOS EN PYTHON:
        - Booleanos
        - Enteros
        - Decimales
        - Texto
        - Listas
        - Tuplas --> Arrays que no permiten la modificación de sus valores
        - Conjuntos (Set) --> Arrays o Listas que no admiten valores repetidos
        - Diccionarios
'''
#Declaración de variables
numero = 6
booleano = False
decimal = 5.3
texto = "Hola"

#Imprimir por pantalla (el print salta de linea automticamente)
print("El número es:" + str(numero)) # --> No deja el espacio en blanco (lo concatena)
print("El número es:" , numero) # --> La coma hace que se deje un espacio en blanco

#Usando el + con un texto y algo que no es un texto dará fallo porque no deja concatenar tipos de datos diferentes
#Para parsearlo usamos str()

'''
    OPERADORES EN PYTHON:
        - Aritmeticos ( + - * / % ** //) --> ** es el exponente y // es la división exacta sin el resto (estos siguen el orden estandar de las operaciones matmáticas)
        - Relacionales ( < > <= >= == !=)
        - Asignación ( = += -= ... )
        - Lógicos ( and or not) --> Preferencia: not / and / or
        - Pertenencia ( in , not in ) Para saber si un valor está dentro de otro o no
        - Identidad ( is ) Para saber si un elemento es o no igual a otro
'''

#Para imprimir sin salto de linea hacemos print("Hola" , end="")

'''
    PARSERS EN PYTHON
    -----------------
        - int()
        - float()
        - str()
        - bool()
        - list()
        - tuple()
        - set()
        - dict()
'''

#Funciones útiles en Python
var = "texto"
print(len(var)) # len() devuelve la longitud de la cadena
print(abs(-5)) # abs() devuelve el valor absoluto del número 
print(round(3.3/3)) #round() devuelve el redondeo --> podemos poner round ( x , 2) en este caso aproxima con 2 decimales
print(eval("5 + 9 * 3")) #eval() hace el calculo de una expresión numérica en formato de texto
print(type(var)) #type() devuelve el tipo de la variable en forma <class 'tipo'>


#Rangos en Python (se pueden escribir de 3 formas)
print(list(range(10))) # --> 0 1 2 3 4 5 6 7 8 9
print(list(range(5,10))) # --> 5 6 7 8 9
print(list(range(1,10,2))) # --> 1 3 5 7 9
#Tenemos que convertir los rangos a listas para ver los datos que tenemos


'''
    ESTRUCTURAS DE CONTROL EN PYTHON
        - If
        - For
        - While
'''
#Los parentesis solo son necesarios si queremos modificar el orden de evalución
if 5<6 :
    print("5<6")
elif 5 == 5 :
    print("5=5")
else :
    print("5>6")
    
 #Usamos rangos y se sigue la estructura del for each
for indice in range(5):
     print(indice)

#Simula la estructura del for     
var="Esto es un texto"
for indice in range(len(var)):
    print(var[indice])

#Más similar a la estructura del for each
for letra in var:
    print(letra)
    
contador = 0    
while contador != 10 :
    print(contador)
    contador+=1
    
'''
    TIPOS DE DATOS POR CONSOLA
        - input() --> Siempre recoge un String
'''

var = int(input("Dame un número --> "))
print("El número es:", var)
print(type(var))