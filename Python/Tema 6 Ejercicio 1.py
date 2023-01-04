"""
·En este ejercicio vais a crear la clase Vehículo la cual tendrá
 los siguientes atributos:
    -Color
    -Ruedas
    -Puertas
·Por otro lado crearéis la clase Coche la cual heredará de Vehículo
 y tendrá los siguientes atributos:
    -Velocidad
    -Cilindrada
·Por último, tendrás que crear un objeto de la clase Coche y
 mostrarlo por consola.
"""

class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas,  velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

bmw = Coche("", 0, 0, 0, 0)
bmw.color = "rojo"
bmw.ruedas = 4
bmw.puertas = 2
bmw.velocidad = 220
bmw.cilindrada = 2200

print(f"\nLas caracteristicas del coche son:\n")
print(f"Es de color {bmw.color}.")
print(f"Tiene {bmw.ruedas} nuevas.")
print(f"Es de {bmw.puertas} puertas.")
print(f"Su velocidad maxima es: {bmw.velocidad}Km/h.")
print(f"Tiene una cilindrada de: {bmw.cilindrada}cc.")