sopaLetras = [
  ['Y', 'W', 'D', 'E', 'N', 'V', 'U', 'D', 'M', 'R'],
  ['A', 'Q', 'C', 'V', 'U', 'J', 'Y', 'O', 'A', 'D'],
  ['O', 'L', 'W', 'T', 'N', 'M', 'G', 'M', 'Z', 'J'],
  ['W', 'E', 'G', 'T', 'G', 'I', 'A', 'P', 'R', 'V'],
  ['F', 'G', 'N', 'U', 'D', 'R', 'X', 'L', 'L', 'B'],
  ['Q', 'J', 'B', 'O', 'R', 'K', 'W', 'X', 'N', 'R'],
  ['K', 'E', 'C', 'O', 'B', 'I', 'I', 'U', 'A', 'I'],
  ['D', 'F', 'R', 'S', 'O', 'L', 'T', 'W', 'W', 'I'],
  ['B', 'P', 'S', 'V', 'P', 'L', 'J', 'M', 'U', 'G'],
  ['K', 'T', 'S', 'V', 'Z', 'O', 'C', 'H', 'O', 'D']]
# Palabras a buscar
palabras = ['PROGRAMAR', 'ALGORITMO', 'DEBUG', 'CODIGO'] 
#Lista de direcciones
direcciones = [ (-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, 1), (-1, -1), (1, -1) ]

#FUNCIÓN RECURSIVA PARA ENCONTRAR LA PALABRA
def comprobarDireccion(palabra, fila, columna, direccion, contador):
    #Si la longitud coincide la palabra está completa
    if contador == len(palabra):
        return True
    
    #Comprobamos si se puede mover en esa direccion (fuera de rango o letra no coincide)
    if (fila < 0 or fila >= len(sopaLetras) or columna < 0 or columna >= len(sopaLetras[0]) 
        or sopaLetras[fila][columna] != palabra[contador]):
        return False
    
    #Si no ocurre nada significa que ha encontrado la letra correcta asi que nos movemos en esa dirección recursivamente
    return comprobarDireccion(palabra, fila + direccion[1], columna + direccion[0], direccion, contador + 1)


#FUNCIÓN PARA BUSCAR LA PALABRA
def buscar_palabra(palabra):
    #Recorremos la lista de la sopa de letras para acceder a cada elemento
    for i in range(len(sopaLetras)):
        for j in range(len(sopaLetras[0])):
            #Vamos comprobando cada dirección recursivamente hasta que comprobamos si se devuelve True
            #Cuando sea True significa que tenemos la palabra, asi que devolvemos la coordenada 
            #y la dirección en la que se mueve
            for direccion in direcciones:
                if comprobarDireccion(palabra, i, j, direccion, 0):
                    return (i, j), direccion
    
    #En caso de llegar a este punto se devuelve None ya que la palabra no se ha encontrado
    return None, None



#Recorremos la lista de palabras y por cada una llamamos a la busqueda de esta, almacenando 
#La coordenada y la direccion
for palabra in palabras:
    coordenada, direccion = buscar_palabra(palabra)

    #Para cada palabra imprimimos los resultados si existen, si no marcamos que no existen las palabras
    if coordenada:
        print("La palabra", palabra, "empieza en la coordenada", coordenada , 
              "y va en la dirección (", direccion[0], ",", direccion[1], ")")
    else:
        print("La palabra", palabra, "no se encuentra en la sopa de letras")

