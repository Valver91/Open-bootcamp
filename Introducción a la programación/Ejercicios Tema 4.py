"""
1·Usando un if, crear una condición que compare si la variable numeroIf 
es positivo, negativo, o 0.
Pista: Los números inferiores a 0 son negativos y los superiores,
positivos.
"""
numeroIf = -7

if numeroIf > 0:
    print("El número es: Positivo")
elif numeroIf < 0:
    print("El número es: Negativo")
else:
    print("El número es: 0")



"""
2·Crea un bucle While, este bucle tendrá que tener como condición que la 
variable numeroWhile sea inferior a 3, el bloque de código que tendrá 
el bucle deberá:
    Incrementar el valor de la variable en uno cada vez que se ejecute.
    Mostrarlo por pantalla cada vez que se ejecute.
"""
numeroWhile = 0

while numeroWhile < 3:
    numeroWhile += 1
    print(numeroWhile)
else:
    print("Ya es mayor de 3")



"""
3·Para el bucle Do While, deberás crear la misma estructura que en el
While, pero solo se debe ejecutar una vez.
"""
numeroDoWhile = 2

while numeroDoWhile < 3:
    numeroDoWhile += 1
    print(numeroDoWhile)
    break
else:
    print("Ya es mayor de 3")



"""
4·Para el bucle For, crea una variable numeroFor, esta variable tendrá 
como valor 0 y su condición será que la variable sea igual o menor
que 3, se irá incrementando en 1 su valor cada vez que se ejecute y
deberá mostrarse por pantalla.
"""
numeroFor = 0
numeroForImp = []

if numeroFor < 3 or numeroFor > 3:
    numeroFor += 1
    numeroForImp.append(numeroFor)
else:
    print("El número ya es 3")
for num in numeroForImp:
    print(numeroForImp)



"""
5·Por último, para el Switch, deberás crear la variable estacion, y
distintos case para las cuatro estaciones del año. Dependiendo del
valor de la variable estacion se deberá mandar un mensaje por consola
informando de la estación en la que está. También habrá que poner un
default para cuando el valor de la variable no sea una estación.
"""
estacion = "invierno"

def primavera():
    print("Estamos en primavera")

def verano():
    print("Estamos en verano")

def otoño():
    print("Estamos en otoño")

def invierno():
    print("Estamos en invierno")

def default():
    print("La estación especificada no es válida")

switcher = {
    "primavera": primavera,
    "verano": verano,
    "otoño": otoño,
    "invierno": invierno
}

funcion = switcher.get(estacion, default)
funcion()