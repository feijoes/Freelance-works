
using System;
namespace PruebaCalseAbstracta
{
    internal class  Program
    {
        private static void Main(string[] args)
        {
            DISCODURO D = new DISCODURO();
            D.Lectura();
            D.Escritura();
            Console.WriteLine("La capacidad del disco duro es " + D.Capacidad);
            Console.WriteLine("El espacio ocupado del disco duro es " + D.EspacioOcupado);

            MEMORIAUSB M = new MEMORIAUSB();
            M.Lectura();
            M.Escritura();
            Console.WriteLine("La capacidad de la memoria USB es " + M.Capacidad);
            Console.WriteLine("El espacio ocupado es " + M.EspacioOcupado);
        }
    }
}