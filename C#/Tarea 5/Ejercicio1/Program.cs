using System.Linq;
internal partial class Program
{
    private static void Main(string[] args)
    {   
        try
        {
            Console.WriteLine("Escriba un numero:");
            string numero = Console.ReadLine();
            if(numero.All(char.IsDigit))
            {
                ;
                
            }
            Console.WriteLine($"Pusiste el numero {numero}");
        }
        catch (System.Exception)
        {
            Console.WriteLine("No es un numero valido");
        }
    }
}