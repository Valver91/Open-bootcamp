"""
·Escribe un programa en la consola de python que pida al usuario su
 peso (en kg) y estatura (en metros), calcule el índice de masa
 corporal y lo almacene en una variable, e imprima por pantalla
 la frase Tu índice de masa corporal es donde es el índice de masa
 corporal calculado redondeado con dos decimales.
""" 

import math

peso = float(input("Introduca su peso en Kg: "))
estatura = float(input("Introduca su estatura en m: "))

imc = peso / (estatura*estatura)
imc = round(imc, 2)

print(f"Tu índice de masa corporal es {imc}")