internal partial class Program
{
    private static void Main(string[] args)
    {
        try
        {
            Console.WriteLine("Primer numero:");
            int numero1 = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Segundo numero:");
            int numero2 = Convert.ToInt32(Console.ReadLine());
             Console.WriteLine($"Los numeros {numero1} y {numero2} son enteros");
        }
        catch (System.FormatException)
        {
            Console.WriteLine("Error: el input inserido no era un numero entero");
        }
    }
}