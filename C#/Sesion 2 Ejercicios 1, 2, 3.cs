/*
·Ejercicio 1:
    Variables Escribe un programa que reciba datos de una persona y genera un mensaje,
    usa una variable para cada dato y otra para el mensaje. 
    Ej: nombre, apellido, edad, sabe programar, etc.
*/

Console.WriteLine("Introduce tu nombre: ");
string nombre = Console.ReadLine();

Console.WriteLine("Introduce tu apellido: ");
string apellido = Console.ReadLine();

Console.WriteLine("Introduce tu edad: ");
string edad = Console.ReadLine();

Console.WriteLine("Responde Si o No, ¿Sabes programar?: ");
string prog = Console.ReadLine();


Console.WriteLine("Hello, " + nombre + " " + apellido + ", tienes " + edad + " años, y " + prog + " sabes programar.");



/*
·Ejercicio 2:
    Tipos Usando los tipos de variables más adecuados, describe los objetos siguientes:
    Coche: puertas, ruedas, marca, ITV vigente
    Mesa: peso, largo, material, color
    Nota: puedes escribir estos datos por consola si prefieres verlos.
    La idea del ejercicio es almacenar los datos en los tipos más adecuados.
*/

class Coche
{
    // Atributos del coche
    public int puertas;
    public int ruedas;
    public string marca;
    public bool ITV_vigente;

    // Métodos para mostrar los datos del coche
    public void MostrarDatos()
    {
        Console.WriteLine("Puertas: " + puertas);
        Console.WriteLine("Ruedas: " + ruedas);
        Console.WriteLine("Marca: " + marca);
        Console.WriteLine("ITV Vigente: " + ITV_vigente);
    }
}

class Mesa
{
    // Atributos de la mesa
    public int peso;
    public int largo;
    public string material;
    public string color;

    // Métodos para mostrar los datos de la mesa
    public void MostrarDatos()
    {
        Console.WriteLine("Peso: " + peso);
        Console.WriteLine("Largo: " + largo);
        Console.WriteLine("Material: " + material);
        Console.WriteLine("Color: " + color);
    }
}



/*
·Ejercicio 3:
    Operadores Determina los operadores para verificar las siguientes condiciones:
    Un número es mayor o igual a 18
    Un char es ‘a’
    Se cumplen dos conciones a la vez (ambas verdaderas)
    Se cumple una de dos condiciones a la vez (una true y otra false)
    Nota: puedes escribir estos datos por consola si prefieres verlos.
    La idea del ejercicio es almacenar los datos en los tipos más adecuados.
*/

Console.WriteLine("Mayor o igual a 18: " + (20 >= 18));
Console.WriteLine("Igual a 'a'? " + ("j" == "a"));

int a = 5;
int b = 12;
Console.WriteLine("Se cumplen dos conciones a la vez (ambas verdaderas)" + (a<10 && b>10));
Console.WriteLine("Se cumple una de dos condiciones a la vez (una true y otra false)" + (a<10 && b<10));


