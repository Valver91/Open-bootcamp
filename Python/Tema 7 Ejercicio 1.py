"""
·En este ejercicio tendréis que crear un módulo que contenga las
 operaciones básicas de una calculadora: sumar, restar, multiplicar
 y dividir.
·Este módulo lo importaréis a un archivo python y llamaréis a las
 funciones creadas. Los resultados tenéis que mostrarlos por consola.
"""

import moduloOperacionesT7Ej1 as mop

def main():
    suma = mop.suma(3, 6)
    resta = mop.resta(3, 6)
    multiplicacion = mop.multiplica(3, 6)
    division = mop.divide(3, 6)
    print(f"\nLos resultados de las operaciones son: ")
    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)

if __name__ == '__main__':
    main()