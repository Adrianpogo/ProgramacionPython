'''
Crear una Clase Almacen que tenga funciones de:
    - Añadir elemento que permita añadir cualquier elemento menos diccionarios
    - getAlmacen que devuelve un diccionario con el tipo de dato como clave y el elemento como valor
'''

class Almacen ():
    def __init__(self):
        self.elementos = dict()

    # Función auxiliar para no repetir código
    def aux_añadir (self,elemento):
        if isinstance(elemento,dict):
            print("No se pueden añadir diccionarios.")
            return
        tipo_dato = elemento.__class__.__name__ # También se puede poner type(elemento).__name__
        if tipo_dato in self.elementos.keys():
            self.elementos[tipo_dato].append(elemento)
        else:
            self.elementos[tipo_dato] = [elemento]

    def añadir_elemento(self, elemento):
        self.aux_añadir(elemento)
        
    def añadir_varios_elementos(self, *elementos):
        for elemento in elementos:
            self.aux_añadir(elemento)

    def get_almacen(self):
        return self.elementos
    

almacen = Almacen()
almacen.añadir_elemento(5)
almacen.añadir_elemento(6)
almacen.añadir_elemento("Hola")
almacen.añadir_elemento([1, 2, 3])
almacen.añadir_elemento(5.5)
almacen.añadir_elemento({"Mario":23})
print(almacen.get_almacen())

almacen.añadir_varios_elementos("Hola0",1,2,3.4,[1,2,3])
print(almacen.get_almacen())