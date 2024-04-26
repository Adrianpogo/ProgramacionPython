class Tarea():
    def __init__(self, id, descripcion, fecha) :
        self.id = id
        self.descripcion = descripcion
        self.fecha = fecha

    
    def get_id(self):
        return self.id
    
    def get_descripcion(self):
        return self.descripcion
    
    def get_fecha(self):
        return self.fecha
    