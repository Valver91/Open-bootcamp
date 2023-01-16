/*
·Ejercicio 1:
    Crea una estructura de datos para un cliente con estos campos:
        Nombre completo
        Teléfono
        Dirección
        Email
         Si es nuevo cliente
    Bonus: escribe un método para presentar estos datos desde la estructura al hacer Console.WriteLine(...)
*/

public struct Cliente
{
    public string nombre;
    public string telefono;
    public string direccion;
    public string Email;
    public bool IsNew;

    public void PrintClient()
    {
        Console.WriteLine("Nombre completo: " + nombre);
        Console.WriteLine("Teléfono: " + telefono);
        Console.WriteLine("Dirección: " + direccion);
        Console.WriteLine("Email: " + Email);
        Console.WriteLine("Es nuevo cliente: " + IsNew);
    }
}