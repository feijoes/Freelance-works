internal partial class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Primer numero:");
        int numero1 = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Segundo numero:");
        int numero2 = Convert.ToInt32(Console.ReadLine());
        try
        {
            Console.WriteLine($"La division de {numero1} y {numero2} es {numero1/numero2}");
        }
        catch (System.DivideByZeroException)
        {
            Console.WriteLine("Error: división por cero");
        }
        
    }
}