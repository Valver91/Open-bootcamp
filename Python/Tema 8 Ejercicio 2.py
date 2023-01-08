"""
·En este segundo ejercicio, tendréis que crear un archivo py y dentro
 crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis
 en un archivo y luego lo cargamos.
"""

archivo = open('prueba.py', 'w')

archivo.write("""class vehiculo:
    def __init__(self):
        pass""")

archivo.close()
