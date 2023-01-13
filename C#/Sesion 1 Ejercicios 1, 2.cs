/*
· Ejercicio 1:
    Escribe un programa que reciba tu nombre y lo escriba por consola.
*/

Console.WriteLine("Introduce tu nombre: ");
string nombre = Console.ReadLine();

Console.WriteLine("Hello, " + nombre);



/*
· Ejercicio 2:
    Escribe un programa que tome la hora y la escriba por pantalla.
*/

var hora = DateTime.Now;

Console.WriteLine("Son las: " + hora);