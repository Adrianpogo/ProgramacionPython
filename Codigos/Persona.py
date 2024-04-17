# Para importar una clase hacemos "import -nombreFichero- from -nombreClase-", en caso de tener una super clase
# si ya se ha importado la clase hija, no es necesario importar el padre  no ser que queramos usar una funcion especifica

class SerVivo ():
    # Cosntructor --> Siempre tiene como primer parámetro el "self", al igual que cualquier función
    def __init__(self, nombre, edad) :
        self.edad = edad
        self.nombre = nombre
        #self.__DNI = dni --> Convertimos el atributo en privado

    # No hay getters y setters, pero la funcionalidad se puede implementar igualmente
    def getEdad (self):
        return self.edad
    
    def setEdad (self, edad):
        self.edad=edad

    def getNombre (self):
        return self.nombre
    
    def setNombre (self, nombre):
        self.nombre=nombre
        

# En () iria una super clase de la que se hereda
class Persona(SerVivo):
    
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    # To String
    def __str__(self) :
        return "Nombre: " + self.nombre + " | Edad: " + str(self.edad)
    
    # Equals --> Se suele comprobar incialmente el tipo de la clase
    def __eq__(self, value) :
        return self.nombre == value.nombre and isinstance(self, Persona) == isinstance(value, Persona)

    def saludar(self):
        print("Hola me llamo", self.nombre)

# Para usar la clase

#p1= Persona 
p1= Persona("Raaul", 19)
p2= Persona("Ruben", 23)
p3= Persona("Ruben", 19)

print("El nombre de p1 es:", p1.getNombre(), "su edad es:", p1.getEdad())
print("El nombre de p2 es:", p2.getNombre(), "su edad es:", p2.getEdad())

p1.setNombre("Raul")

p1.saludar()
p2.saludar()

# Podemos imprimirlo pero es necesario sobreescribir __str__ ya que es la función que tiene en cuenta
print(p1)
print(p2)

# Podemos igualarlos, pero es necesario sobreescribir __eq__ en este caso serán iguales si tienen el mismo nombre
print(p1==p2)
print(p2==p3)


