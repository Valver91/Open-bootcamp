"""
·Crear clase Persona.
·Crear variables las privadas edad, nombre y telefono de la clase Persona.
·Crear gets y sets de cada propiedad.
·Crear un objeto persona en el main.
·Utiliza los gets y sets para darle valores a las propiedades edad,
 nombre y telefono, por último muéstralas por consola.
"""

class Persona:
    def __init__(self, edad, nombre, telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, telefono):
        self.__telefono = telefono

if __name__ == '__main__':
    persona = Persona(0, '', 0)
    persona.edad = 31
    persona.nombre = "Santiago"
    persona.telefono = 600000009

    print(f"Edad: {persona.edad},\nNombre: {persona.nombre},\nTelefono: {persona.telefono}")