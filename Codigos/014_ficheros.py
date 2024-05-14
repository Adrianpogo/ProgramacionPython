'''
P1 - Ruta --> Se crea en la ruta relativa, en donde esté el fichero 014_ficheros.py
P2 - Modo --> El modo en el que se abre un fichero

                - r para modo lectura
                - a para agregar texto 
                - w para escribir un fichero (desde 0)

                Si el fichero no existe, con a y w se crea, pero con r dará error

P3 - Encoding --> Se especifica la codificación para aceptar caracteres especiales
'''


# Si intentamos leer sin el fichero saltará la excepción
try:
    with open("./ejemplo.txt","r",) as archivo: 
        print(archivo.read())
except IOError as e:
    print("ERROR en la lectura del archivo" + str(e))

# Escribir desde 0
try:
    with open("./ejemplo.txt","w", encoding="UTF-8") as archivo: 
        archivo.write("Hola buenos días!")
        print("¡Fichero escrito con éxito!")
except IOError as e:
    print("ERROR en la escritura del archivo" + str(e))

# Sobreescribir
try:
    with open("./ejemplo.txt","a", encoding="UTF-8") as archivo: 
        archivo.write("\nMe llamo Lucas")
        print("¡Fichero escrito con éxito!")
except IOError as e:
    print("ERROR en la escritura del archivo" + str(e))


try:
    with open("./ejemplo.txt","r") as archivo: 
        print(archivo.read())
except IOError as e:
    print("ERROR en la lectura del archivo" + str(e))

