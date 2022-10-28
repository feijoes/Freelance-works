internal partial class Program
{
    private static void Main(string[] args)
    {   
       
        Console.WriteLine("Escriba un numero:");
        var input = Console.ReadLine();
        if (int.TryParse(input, out int number1)) {
            Console.WriteLine($" Pusiste {number1} ");
        }
        else
        {
            Console.WriteLine($"\"{input}\" no es valido");
        }
        
       
    }
}