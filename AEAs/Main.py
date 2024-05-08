from Producto import Producto
from MaquinaExpendedora import MaquinaExpendedora

# Creación de los objetos para probar
maquina_expendedora = MaquinaExpendedora()
pro1 = Producto("Patatas", 1.75, 3)
pro2 = Producto("Monster", 2.5, 4)
pro3 = Producto("PATATAS", 1.75, 3)

# Comprobación de la función __str__
print(pro1)

# Comprobación de la función __eq__
print(pro1 == pro2)
print(pro1 == pro3)
print()

# Comprobación de añadir productos (nuevos y existentes)
maquina_expendedora.añdir_producto_inventario(pro1, 2)
maquina_expendedora.añdir_producto_inventario(pro1, 2)
maquina_expendedora.añdir_producto_inventario(pro2, 4)
print()

# Comprobación de impresión de productos
maquina_expendedora.imprimir_lista()
print()

# Comprobación de reducción de productos
maquina_expendedora.reducir_un_producto(pro1)
maquina_expendedora.imprimir_lista()
print()

# Comprobación de compras con conduciones (compra buena y errónea)
maquina_expendedora.comprar_con_comprobaciones(pro1 , 2.5)
maquina_expendedora.comprar_con_comprobaciones(pro2 , 1.5)

