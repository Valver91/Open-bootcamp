"""
·En este segundo ejercicio, tendréis que crear un programa que tenga
 una clase llamada Alumno que tenga como atributos su nombre y su nota.
 Deberéis de definir los métodos para inicializar sus atributos,
 imprimirlos y mostrar un mensaje con el resultado de la nota y si
 ha aprobado o no.
"""

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def nota(self):
        return self.__nota
    @nota.setter
    def nota(self, nota):
        self.__nota = nota
        
def aprovado(nota):
    if nota not in range(0, 11):
        print("La nota tiene que estar entre el 0 y el 10.")
    elif nota >= 5:
        return "Aprovado"
    else:
        return "Suspendido"


if __name__ == '__main__':
    alumno = Alumno('', 0)
    alumno.nombre = "Santiago"
    alumno.nota = 7.2

    print(f"\nEl alumno: {alumno.nombre}\nestá: {aprovado(alumno.nota)}")