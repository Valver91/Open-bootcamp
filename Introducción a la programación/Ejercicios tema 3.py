"""Primera parte.
·Crear una función con tres parámetros que sean números 
 que se suman entre sí.
·Llamar a la función en el main y darle valores
""" 

def suma(num1, num2, num3):
    resultado = num1 + num2 + num3

    return resultado

resultado = suma(1, 2, 3)
print(resultado)

"""Segunda parte.
·Crear una clase coche.
·Dentro de la clase coche, una variable numérica que almacene 
 el número de puertas que tiene.
·Una función que incremente el número de puertas que tiene el coche.
·Crear un objeto miCoche en el main y añadirle una puerta.
·Mostrar el número de puertas que tiene el objeto.
"""

class Coche:
    def __init__(self, puertas: int):
        self.puertas = puertas

    def sumar_puerta(self):
        self.puertas += 1

miCoche = Coche(5)
miCoche.sumar_puerta()

print(miCoche.puertas)