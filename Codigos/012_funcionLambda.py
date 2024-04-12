'''
Permite hacer funciones anonimas que recibe los parámetros que sean necesarios y realiza las operaicones en 1 linea

--> lambsa "lista de parametros" : funcion a realizar

Se usan para evitar declarar excesivas funciones que realmente usamos pocas veces y son pequeñas

'''

numeros=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x: x%2==0 and x>5, numeros)))

#Se pueden dar nombres a las funciones anonimas
sumar = lambda x: x+1
print(list(map(sumar,numeros)))