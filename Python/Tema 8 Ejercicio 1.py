"""
·En este ejercicio, tendréis que crear un archivo py donde creéis
 un archivo txt, lo abráis y escribáis dentro del archivo. Para ello,
 tendréis que acceder dos veces al archivo creado.
"""

archivo = open('prueba.txt', 'w')
archivo.write('Soy la prueba de que el programa escribe en el archivo')
archivo.close()