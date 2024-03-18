import math
"""
Ejercicio 1:
Crear un programa que calcule el área de un triángulo rectángulo dado su base y altura.
Utiliza variables para almacenar la base, la altura y el resultado del cálculo del área.
"""
print("\n>> EJERCICIO 1")
print()

base = 2.45
altura = 4.5
area = (base * altura) / 2
print("El área del triángulo es:" , round(area,2))

print("-------------------------------------------")
print()

"""
Ejercicio 2:
Escribir un programa que convierta grados Celsius a grados Fahrenheit.
Utiliza una variable para almacenar los grados Celsius, realiza el cálculo y muestra el resultado.
"""
print(">> EJERCICIO 2")
print()

celsius = 30
fahrenheit = celsius * (9/5) + 32
print(celsius , "º celsius son" , fahrenheit , "º fahrenheit") 

print("-------------------------------------------")
print()

"""
Ejercicio 3:
Crear un programa que calcule el perímetro y el área de un círculo dado su radio.
Utiliza una variable para almacenar el radio, realiza los cálculos y muestra los resultados.
"""
print(">> EJERCICIO 3")
print()

radio = 3.46
perimetro = 2 * math.pi * radio
area = 3.14 * (radio**2)
print("El perímetro es:" , round(perimetro,2))
print("El área es:" , round(area,2))

print("-------------------------------------------")
print()

"""
Ejercicio 4:
Escribir un programa que determine si un número dado es par o impar.
Utiliza una variable para almacenar el número, aplica el operador de módulo y muestra el resultado.
"""
print(">> EJERCICIO 4")
print()

numero = 5
if numero%2 == 0:
    print("El número" , numero , "es par")
else:
    print("El número" , numero , "es impar")
    
print("-------------------------------------------")
print()

"""
Ejercicio 5:
Crear un programa que calcule la hipotenusa de un triángulo rectángulo dado sus catetos.
Utiliza dos variables para almacenar los catetos, aplica el teorema de Pitágoras y muestra el resultado.
"""
print(">> EJERCICIO 5")
print()

catetoA = 4
catetoB = 6
hipotenusa = math.sqrt(catetoA**2 + catetoB**2)
print("La hipotenusa de un triángulo cuyos catetos son" , catetoA , "y" , catetoB , "es:" , round(hipotenusa,2))

print("-------------------------------------------")
print()

"""
Ejercicio 6:
Crear un programa que calcule el área y el perímetro de un rectángulo dados su base y su altura.
Utiliza variables para almacenar la base, la altura y realiza los cálculos correspondientes.
"""
print(">> EJERCICIO 6")
print()

base= 3.4
altura = 2.7
perimetro = base*2 + altura*2
area = base * altura
print("El perímetro del rectángulo es:" , round(perimetro,2))
print("El área del rectángulo es:", round(area,2))

print("-------------------------------------------")
print()

"""
Ejercicio 7:
Escribir un programa que determine si un año es bisiesto o no.
Utiliza una variable para almacenar el año, aplica las reglas para determinar si es bisiesto y muestra el resultado.
"""
print(">> EJERCICIO 7")
print()

año = 2032
if año%4 == 0:
    print(año , "es un año bisiesto")
else:
    print(año , "no es un año bisiesto")
    
print("-------------------------------------------")
print()


"""
Ejercicio 8:
Crear un programa que convierta una cantidad de dólares a euros.
Utiliza una variable para almacenar la cantidad de dólares, realiza la conversión y muestra el resultado.
"""
print(">> EJERCICIO 8")
print()

dolares = 56.7
euros = dolares * 0.92
print(dolares , "$ son" , euros , "€")

print("-------------------------------------------")
print()

"""
Ejercicio 9:
Escribir un programa que determine si un número dado es positivo, negativo o cero.
Utiliza una variable para almacenar el número, aplica condiciones y muestra el resultado.
"""
print(">> EJERCICIO 9")
print()

numero = -4
if numero < 0 :
    print(numero , "es negativo")
elif numero > 0 :
    print(numero , "es positivo")
else:
    print(numero , "es 0 exacto")
    
print("-------------------------------------------")
print()

"""
Ejercicio 10:
Crear un programa que calcule el promedio de tres números dados.
Utiliza tres variables para almacenar los números, realiza el cálculo y muestra el resultado.
"""
print(">> EJERCICIO 10")
print()

numero1 = 9
numero2 = 3
numero3 = 7
promedio = (numero1+numero2+numero3) / 3
print("El promedio de (" , numero1 , "," , numero2 , "," , numero3 , ") es:" , round(promedio,2))

print("-------------------------------------------")
print()

"""
Ejercicio 11:
Crear un programa que determine si un número dado es primo o no.
Utiliza una variable para almacenar el número, aplica las reglas para determinar si es primo y muestra el resultado.
"""
print(">> EJERCICIO 11")
print()

numero = 18
for i in range(2,numero):
    if (numero%i) == 0:
      print(numero , "no es un número primo" , i , "es divisor")
      break
  
    print(numero , "es un número primo")
    break

print("-------------------------------------------")
print()

"""
Ejercicio 12:
Escribir un programa que determine si un número dado es múltiplo de otro.
Utiliza dos variables para almacenar los números, aplica el operador de módulo y muestra el resultado.
"""
print(">> EJERCICIO 12")
print()

numero1 = 4
numero2 = 17

if numero2%numero1 == 0 :
    print(numero2 , "es múltiplo de" , numero1)
else:
    print(numero2 , "no es múltiplo de" , numero1)
    
print("-------------------------------------------")
print()

"""
Ejercicio 13:
Crear un programa que calcule el factorial de un número dado.
Utiliza una variable para almacenar el número, realiza el cálculo del factorial y muestra el resultado.
"""
print(">> EJERCICIO 13")
print()

numero = 10
factorial = 1

for i in range(0,numero):
    factorial += factorial * i
print("El factorial de" , numero , "es:" , factorial)

print("-------------------------------------------")
print()

"""
Ejercicio 14:
Escribir un programa que determine si una cadena de texto es palíndromo o no.
Utiliza una variable para almacenar la cadena, aplica condiciones y muestra el resultado.
"""
print(">> EJERCICIO 14")
print()

cadena = "aabcbaa"
indiceInverso = len(cadena)

for i in range(0 , int(len(cadena)/2)):
    if cadena[i] != cadena[indiceInverso-1]:
        esPalindromo = False
        break
    else:
        esPalindromo = True
        
    indiceInverso -= 1
    

if esPalindromo :
    print(cadena , "es palíndromo")
else :
    print(cadena , "no es palíndromo")


print("-------------------------------------------")
print()

"""
Ejercicio 15:
Crear un programa que cuente la cantidad de vocales en una cadena de texto dada.
Utiliza una variable para almacenar la cadena, itera sobre cada carácter y cuenta las vocales, luego muestra el resultado.
"""
print(">> EJERCICIO 15")
print()

cadena = "Esto es un texto de EjemplO"
vocales = "aeiouAEIOU"
contador = 0

for letra in cadena:
    if letra in vocales :
        contador += 1

print("El número de vocales de '" , cadena , "' es:" , contador)

print("-------------------------------------------")
print()

"""
Ejercicio 16:
Escribir un programa que determine si una cadena de texto dada es un pangrama o no.
Un pangrama es una frase que contiene todas las letras del alfabeto al menos una vez.
Utiliza una variable para almacenar la cadena, itera sobre cada letra y verifica si está presente en el alfabeto, luego muestra el resultado.
"""
print(">> EJERCICIO 16")
print()

texto1 = "Esto no es una oracion pangrama"
texto2 = "El cadáver de wamba, rey godo de España  fue exhumado y trasladado en una caja de zinc que peso un kilo"
alfabeto = "abcdefghijklmnñopqrstuvwxyz"
alfabetoAux = ""

for letra in texto2:
    if alfabeto.__contains__(letra) and  not alfabetoAux.__contains__(letra):
        alfabetoAux += letra
        
if len(alfabeto) == len(alfabetoAux):
    print("Es un texto pangrama")
else:
    print("No es un texto pangrama")


print("-------------------------------------------")
print()

"""
Ejercicio 17:
Escribir un programa que calcule el máximo común divisor (MCD) de dos números enteros.
Utiliza dos variables para almacenar los números, aplica el algoritmo de Euclides y muestra el resultado.
"""
print(">> EJERCICIO 17")
print()
"""
# Pedir al usuario que ingrese los dos números
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

# Calcular el MCD utilizando el algoritmo de Euclides
while num2 != 0:
    temp = num2
    num2 = num1 % num2
    num1 = temp

# El MCD estará almacenado en num1
print("El máximo común divisor (MCD) es:", num1)
"""
print("-------------------------------------------")
print()

"""
Ejercicio 18:
Crear un programa que calcule la potencia de un número dado elevado a otro número entero.
Utiliza dos variables para almacenar la base y el exponente, realiza el cálculo de la potencia y muestra el resultado.
"""
print(">> EJERCICIO 18")
print()

base = 5
exponente = 3
resultado = base**exponente
print("El resultado es:" , resultado)

print("-------------------------------------------")
print()

"""
Ejercicio 19:
Escribir un programa que calcule el área de un círculo dado su radio, utilizando una función.
La función debe recibir el radio como argumento y devolver el área del círculo.
"""
print(">> EJERCICIO 19")
print()

def calcularArea(radio):
    return round(math.pi * radio**2, 2)

print("El área de un circulo de radio 0.8 es:" , calcularArea(0.8))

print("-------------------------------------------")
print()

"""
Ejercicio 20:
Crear un programa que determine si un número dado es perfecto o no.
Un número perfecto es aquel que es igual a la suma de sus divisores propios positivos (excluyendo al propio número).
Utiliza una variable para almacenar el número, realiza los cálculos y muestra el resultado.
"""
print(">> EJERCICIO 20")
print()

numero = 28
print("El número es:" , numero)
contador = 0
i=1

while i < numero:
    if numero % i == 0:
        contador+=i
    i+=1

print("La suma de sus divisores es:" , contador)

if contador == numero :
    print(numero, "es un número perfecto")
else:
    print(numero, "no es un número perfecto")

print("-------------------------------------------")
print()
