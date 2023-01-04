"""
·En este segundo ejercicios tendréis que crear un script que nos diga
 si es la hora de ir a casa. Tendréis que hacer uso del modulo time.
 Necesitaréis la fecha del sistema y poder comprobar la hora.
·En el caso de que sean más de las 7, se mostrará un mensaje y en caso
 contrario, haréis una operación para calcular el tiempo que queda
 de trabajo.
"""

import time

hora_segundos = time.time()
hora_local = time.localtime(hora_segundos)
hora = hora_local.tm_hour
minutos = hora_local.tm_min
segundos = hora_local.tm_sec
hora_sistema = f"{hora}:{minutos}:{segundos}"

if hora_sistema >= f"19:00:00" or hora_sistema <= f"09:00:00":
    print("Horario no laboral")
elif hora_sistema <= f"19:00:00" or hora_sistema >= f"09:00:00":
    hora_final = f"19:00:00"
    hora_restante = hora_final - hora_sistema

    print("Estas en horario laboral")
    print(f"Quedan {hora_restante} de trabajo")
