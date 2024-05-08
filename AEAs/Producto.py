class Producto():
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    
    # Reescritura de la función str
    def __str__(self) :
        return "Nombre: "+ self.nombre + "| Precio: " + str(self.precio) + "€ | Cantidad :"+ str(self.cantidad)
    
    # Reescritura de la función eq
    def __eq__(self, producto) :
        return self.nombre.lower() == producto.get_nombre().lower()
    
    # Getters y Setter auxiliares
    def get_nombre(self):
        return self.nombre
    
    def get_precio(self):
        return self.precio
    
    def get_cantidad(self):
        return self.cantidad
    
    def set_cantidad(self, cantidad):
        self.cantidad=cantidad