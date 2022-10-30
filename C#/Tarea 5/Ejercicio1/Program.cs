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
                string numero ="";
                Console.Write("Digite una numero: ");
                numero = Console.ReadLine();
                if(numero !="")
                {
                    O = 1;
                }
                if(O != 0)
                {
                    try
                    {
                        int result =int.Parse(numero);
                        Console.Write("Numero: "+ numero);
                        O = 1;
                    }
                    catch
                    {
                        Console.Clear();
                        Console.Write(numero + " no es un numero");
                        O = 0;
                    }
                    Console.Read();
                }
            }
            while(O == 0);
        }
    }
}