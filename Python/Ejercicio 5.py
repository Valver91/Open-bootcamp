"""
·Escribe una función que pueda decirte si un año (número entero) es
 bisiesto o no.
"""

def verifica_año_bisiesto(year):

    if year not in range(1, 9999):
        print("No es un año valido, tiene que estar entre el 1 y el 9999.")
    elif (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print(f"El año {year} si es bisiesto.")
    else:
        print(f"El año {year} no es bisiesto.")

verifica_año_bisiesto(int(input("Introduzca año a verificar: ")))