/*
·Ejercicio 1: If
    Escribe un programa que:
    Pida datos a un cliente: Nombre, email, cupón
    Determine si un cliente tiene un cupon descuento
    Muestre un precio rebajado en función del descuento
    Muestre el precio de un producto sin descuento si no hay cupón
    Nota: puedes poner un precio fijo de un producto o uno variable.
*/

double precio = 100.0;
double precioDescuento;

Console.WriteLine("Introduce tu nombre: ");
string nombre = Console.ReadLine() ?? "";

Console.WriteLine("Introduce tu email: ");
string apellido = Console.ReadLine()  ?? "";

Console.WriteLine("¿Tienes cupon de descuento? (S/N) ");
string cupon = Console.ReadLine().ToUpper();
if (cupon == "S")
{
    
    precioDescuento = precio - (precio * 0.1);
    Console.WriteLine("El precio de tu producto con el descuento es de: " + precioDescuento + " €.");
}
else
{
    
    Console.WriteLine("El precio de tu producto sin descuento es de:  " + precio + " €.");
}



/*
·Ejercicio 2: Switch
    Haz una lista de lenguajes de programación, por ejemplo: C#, Java, C++.
    Presenta la lista en consola y pide que el usuario seleccione
    el lenguaje mediante 1, 2, 3 o a, b, c. Presenta el resultado en consola.
    Nota: puedes añadir al resultado el “Hola, mundo” para el caso de C#.
*/

List<string> miLista = new List<string> {"C#", "C", "Java", "C++", "JavaScript", "Python", "PHP"};

Console.WriteLine("Selecciona el legunaje midiante 1, 2, 3...:  ");
int n = Convert.ToInt32(Console.ReadLine());

switch (n)
{
    case 0:
        Console.WriteLine(miLista[0] + "  Hola, mundo");
        break;
    case 1:
        Console.WriteLine(miLista[1]);
        break;
    case 2:
        Console.WriteLine(miLista[2]);
        break;
    case 3:
        Console.WriteLine(miLista[3]);
        break;
    case 4:
        Console.WriteLine(miLista[4]);
        break;
    case 5:
        Console.WriteLine(miLista[5]);
        break;
    case 6:
        Console.WriteLine(miLista[6]);
        break;
    
    default:
        Console.WriteLine("Opción no válida");
        break;
}