"""
·En este segundo ejercicios tendréis que crear un script que nos diga
 si es la hora de ir a casa. Tendréis que hacer uso del modulo time.
 Necesitaréis la fecha del sistema y poder comprobar la hora.
·En el caso de que sean más de las 7, se mostrará un mensaje y en caso
 contrario, haréis una operación para calcular el tiempo que queda
 de trabajo.
"""

import time

current_time = time.localtime()

if current_time.tm_hour >= 19:
    print("Horario no laboral")
else:
    print("Es horario laboral")

time_left = 19 - current_time.tm_hour
print(f"Aún quedan {time_left} horas de trabajo")