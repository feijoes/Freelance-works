using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace ConsoleApp21{
    class Program
    {
        static void Main(string[] args)
        {
            int O = 1;
            do
            {
                Console.Clear();
                string LETRA ="";
                Console.Write("Digite una letra: ");
                LETRA = Console.ReadLine();
                if(LETRA !="")
                {
                    O = 1;
                }
                if(O != 0)
                {
                    try
                    {
                        int result =int.Parse(LETRA);
                        Console.Write("No se permiten numeros....");
                        O = 0;
                    }
                    catch
                    {
                        Console.Clear();
                        Console.Write("Letras: "+ LETRA);
                    }
                    Console.Read();
                }
            }
            while(O == 0);
        }
    }
}