from Tarea import Tarea
import datetime as dt

class Aplicacion ():
    
    def __init__(self) :
        self.tareas_completadas = dict()
        self.tareas_pendientes = list()


    
    def mostrar_menu (self):
        print("\n\n>>  LISTA DE TAREAS  <<\n")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Completar tarea")
        print("4. Mostrar tareas pendientes")
        print("5. Salir")
        print("-----------------------------------")
    
    def comprobar_tarea(self):
        self.mostrar_tareas_pendientes()
        id = input("\nIntroduce el ID de la tarea: ")

        for tarea in self.tareas_pendientes:
            if tarea.get_id() == id:
                return tarea


    # Función para añadir una tarea
    def agregar_tarea(self):
        print("\n --> Agregando tarea...")
        id = input("Introduce el ID de la tarea: ")
        descripcion = input("Introduce la descripción de la tarea: ")

        # Verificar si el ID ya existe
        id_existente = False
        for tarea in self.tareas_pendientes:
            if tarea.get_id() == id:
                id_existente = True
                break

        # Si el ID no existe añadimos la tarea a la lista
        if not id_existente:
            tarea = Tarea(id, descripcion, dt.datetime.now())
            self.tareas_pendientes.append(tarea)
            print("\nTarea agregada con éxito.")
        else:
            print("\nEl ID de la tarea ya existe. Introduce un ID único.")



    # Función para mostrar la lista de tareas pendientes
    def mostrar_tareas_pendientes (self):
        print("\n --> Mostrando tareas pendientes...\n")
        for tarea in self.tareas_pendientes:
            print(tarea.get_id(),"-", tarea.get_descripcion())
    


    # Función para mostrar la lista de tareas completas
    def mostrar_tareas_completadas (self):
        print("\n --> Mostrando tareas completadas...\n")
        for tarea,fecha in self.tareas_completadas.items():
            print(tarea ,"-- Completada: ", fecha)



    # Función para marcar una tarea como completa
    def completar_tarea(self):
        print("\n --> Compleando tarea...")
        tarea = self.comprobar_tarea()
        if tarea:
            dict_aux ={tarea.get_descripcion(): tarea.get_fecha()}
            self.tareas_completadas.update(dict_aux)
            self.tareas_pendientes.remove(tarea)
            print("\nTareas completadas:")
            self.mostrar_tareas_completadas()
        else:
            print("No se ha encontrado ninguna tarea con este ID")
        


    # Función para eliminar una tarea
    def eliminar_tarea(self):
        print("\n --> Eliminando tarea...")
        tarea = self.comprobar_tarea()
        if tarea:
            self.tareas_pendientes.remove(tarea)
        else:
            print("No se ha encontrado ninguna tarea con este ID") 




app = Aplicacion()
while True:
    app.mostrar_menu()

    opcion = int(input("\n Seleccione una opcion: "))
    if opcion == 1:
        app.agregar_tarea()
    elif opcion == 2:
        app.eliminar_tarea()
    elif opcion == 3:
        app.completar_tarea()
    elif opcion == 4:
        app.mostrar_tareas_pendientes()
    elif opcion == 5:
        break
print("\n!Hasta la próxima¡")