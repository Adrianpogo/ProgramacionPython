class MaquinaExpendedora ():
    
    # Constructor
    def __init__(self) :
        self.lista_productos = list()

    # Función para añadir un producto al inventario
    def añdir_producto_inventario(self, producto, cantidad):
        # Si el producto no está en la lista lo añadimos con la cantidad deseada
        if producto not in self.lista_productos:
            producto.set_cantidad(cantidad)
            self.lista_productos.append(producto)
        
        # Si el producto ya existe obtenemos su indice para saber su cantidad y de esta forma modificarla 
        else:
            indice = self.lista_productos.index(producto)
            self.lista_productos[indice].set_cantidad(self.lista_productos[indice].get_cantidad()+cantidad)
            
    # Función para reducir un uno la cantidad del producto
    def reducir_un_producto(self, producto):
        # Comprobamos si está en la lista
        if producto not in self.lista_productos:
            print("No se puede reducir porque no existe el producto")
        else:
            # Encontramos su posición y modificamos su cantidad
            indice = self.lista_productos.index(producto)
            if self.lista_productos[indice].get_cantidad() == 0 :
                print("No se puede reducir más su cantidad")
            else:
                self.lista_productos[indice].set_cantidad(self.lista_productos[indice].get_cantidad()-1)

    # Función para imprimir la lista de productos
    def imprimir_lista(self):
        print(">> Inventario")
        for producto in self.lista_productos:
            print(producto)

    # Función para comprar un producto
    def comprar_con_comprobaciones(self, producto, saldo):
        # Primero comprobamos que el producto existe
        # Si existe comprobamos que hay suficiente cantidad
        # Si hay suficiente cantidad comprobamos que el saldo es suficiente para el precio del producto

        if producto in self.lista_productos:
            indice = self.lista_productos.index(producto)
            if self.lista_productos[indice].get_cantidad() >= 1 and self.lista_productos[indice].get_precio() <= saldo:
                print("\nCompra realizada con éxito!")
                self.reducir_un_producto(producto)
                self.imprimir_lista()
                
            else:
                print("\nERROR: Saldo insuficiente o stock agotado")
        else:
            print("\nERROR: El producto no existe en la máquina")