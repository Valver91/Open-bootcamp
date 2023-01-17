/*
·Ejercicio 1: - While
    Escribe una tabla de multiplicar del 1 al 10 para un número entero que
    recibe por consola. Es decir, un programa que presente para el 1:
    1 x 1 = 1
    1 x 2 = 2
    …
    1 x 10 = 10
*/

Console.WriteLine("Introduce numero para hacer tabla de multiplicar: ");
int n = Convert.ToInt32(Console.ReadLine());

int i = 1;
while(i <= 10)
{
    Console.Write(i * n + " ");
    i++;
}

/*
·Ejercicio 2: - Do while
    Escribe un programa que realice estos pasos:
    Reciba al menos un número por consola
    Determine si el número es positivo o negativo
    Presente un contador para cada tipo (positivo y negativo).
    Nota: el cero se puede abordar en una clase adicional ya que no es
    ni positivo ni negativo. Tienes completa libertad para
    elegir el formato de la salida.
*/

int positiveCount = 0;
int negativeCount = 0;
int zeroCount = 0;
int num;

//El bucle se detendrá cuando el número ingresado sea 000.

do
{
    Console.WriteLine("Introduce número a determinar: ");
    num = Convert.ToInt32(Console.ReadLine());

    if (num > 0)
    {
        positiveCount++;
    }
    else if (num < 0)
    {
        negativeCount++;
    }
    else
    {
        zeroCount++;
    }

} while (num != 000);

Console.WriteLine("Contador de números positivos: " + positiveCount);
Console.WriteLine("Contador de números negativos: " + negativeCount);
Console.WriteLine("Contador de números ceros: " + zeroCount);

//El bucle se detendrá cuando el número ingresado sea 000.




/*
·Ejercicio 3 - For
    Escribe un programa que realice estos pasos:
    Reciba 3 datos:
        ancho
        alto
        relleno o no
    Dibuje en consola con un mismo caracter, por ejemplo *, un rectángulo de las
    dimensiones introducidas y use el tercer dato para discernir
    si el rectángulo está relleno (tiene más * dentro) o no.
    En caso de recibir el mismo número n dos veces debe dibujar un cuadrado de lado n.
    Reto: Extiende el programa anterior para recibir otro número que sea el
    número de cuadrados o rectángulos que se deben dibujar en la pantalla. Ejemplos:
    Input: 2,2,2, relleno = true
    Output:
        ** **
        ** **
    Input: 3, 4, 1, relleno = false
    Output:
        ***
        * *
        * *
        ***
*/


int ancho, alto, numCuadrados,numDibujos;
bool relleno;
char caracter;

Console.WriteLine("Introduce el ancho: ");
ancho = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Introduce el alto: ");
alto = Convert.ToInt32(Console.ReadLine());

if (ancho == alto)
{
    Console.WriteLine("Dibujando un cuadrado de lado " + ancho);
}
else
{
    Console.WriteLine("Dibujando un rectángulo de " + ancho + " de ancho y " + alto + " de alto");
}

Console.WriteLine("¿Desea rellenar el rectángulo/cuadrado? (S/N) ");
string respuesta = Console.ReadLine().ToUpper();
if (respuesta == "S")
{
    relleno = true;
}
else
{
    relleno = false;
}

Console.WriteLine("Introduce el caracter que deseas utilizar para dibujar: ");
caracter = char.Parse(Console.ReadLine());

Console.WriteLine("Introduce el número de cuadrados/rectángulos a dibujar: ");
numDibujos = int.Parse(Console.ReadLine());

for (int i = 1; i <= numDibujos; i++)
{
    if (relleno)
    {
        for (int j = 1; j <= alto; j++)
        {
            for (int k = 1; k <= ancho; k++)
            {
                Console.Write(caracter);
            }
            Console.WriteLine();
        }
    }
    else
    {
        for (int j = 1; j <= alto; j++)
        {
            for (int k = 1; k <= ancho; k++)
            {
                if (j == 1 || j == alto || k == 1 || k == ancho)
                {
                    Console.Write(caracter);
                }
                else
                {
                    Console.Write(" ");
                }
            }
            Console.WriteLine();
        }
    }
    Console.WriteLine();
}
