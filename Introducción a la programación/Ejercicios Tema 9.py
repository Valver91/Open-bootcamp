"""
·Crea una clase Persona con las siguientes variables:
    -La edad.
    -El nombre.
    -El teléfono.
·Una vez creada la clase, crea una nueva clase Cliente que herede de
 Persona, esta nueva clase tendrá la variable credito solo para esa clase.
·Crea ahora un objeto de la clase Cliente que debe tener como
 propiedades la edad, el telefono, el nombre y el credito, tienes que
 darles valor y mostrarlas por pantalla.
·Una vez hecho esto, haz lo mismo con la clase Trabajador que herede
 de Persona, y con una variable salario que solo tenga la
 clase Trabajador.
"""

class Persona:
    def __init__(self, edad, nombre, telefono):
        self.edad = edad
        self.nombre = nombre
        self.telefono = telefono
    
class Cliente(Persona):
    def __init__(self, edad, nombre, telefono, credito):
        super().__init__(edad, nombre, telefono)
        self.credito = credito


cliente = Cliente(31, '', 0, 0)
cliente.edad = 31
cliente.nombre = "Santiago"
cliente.telefono = 600000009
cliente.credito = 1000
print(f"Datos del cliente:\nEdad: {cliente.edad},\nNombre: {cliente.nombre},\nTelefono: {cliente.telefono},\nCredito: {cliente.credito}\n\n")

class Trabajador(Persona):
    def __init__(self, edad, nombre, telefono, salario):
        super().__init__(edad, nombre, telefono)
        self.salario = salario

trabajador = Trabajador(31, '', 0, 0)
trabajador.edad = 35
trabajador.nombre = "Fernando"
trabajador.telefono = 600020009
trabajador.salario = 2000
print(f"Datos del Trabajador:\nEdad: {trabajador.edad},\nNombre: {trabajador.nombre},\nTelefono: {trabajador.telefono},\nSalario: {trabajador.salario}\n\n")
