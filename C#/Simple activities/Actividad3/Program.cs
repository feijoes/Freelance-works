namespace PruebaInterfaz2
{
    internal partial class Program
    {
        private static void Main(string[] args)
        {
            RECTANGULO R = new RECTANGULO(5,4);
            Console.WriteLine("El valor de la base es: "+R.getBase());
            Console.WriteLine("El valor de la altura es: "+R.getAltura());
            Console.WriteLine("El valor de la area es: "+R.CALCULARAREA());
            Console.WriteLine("El valor del perimetro es: "+R.CALCULARPERIMETRO());
            CUADRADO C = new CUADRADO(5);
            Console.WriteLine("El valor de los lados son: "+C.getLado());
            Console.WriteLine("El valor de la area es: "+C.CALCULARAREA());
            Console.WriteLine("El valor del perimetro es: "+C.CALCULARPERIMETRO());
            ROMBO Ro = new ROMBO(5,4);
            Console.WriteLine("El valor de la diagonal Mayor es: "+Ro.getDiagonalMayor());
            Console.WriteLine("El valor de la diagonal Menor es: "+Ro.getDiagonalMenor());
            Console.WriteLine("El valor de la area es: "+Ro.CALCULARAREA());
            Console.WriteLine("El valor del perimetro es: "+Ro.CALCULARPERIMETRO());
        }
    }
}