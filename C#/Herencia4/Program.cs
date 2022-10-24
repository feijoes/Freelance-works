using Herencia4;
internal class Program
{
    private static void Main(string[] args)
    {
        // Probar Shape
        Shape shape1 = new Shape();
        Console.WriteLine($"Color shape1 {shape1.getColor()}");
        shape1.setColor("green");
        Console.WriteLine($"New Color shape1 {shape1.getColor()}");
        Console.WriteLine($"Filled shape1 {shape1.isFilled()}");
        shape1.setFilled(false);
        Console.WriteLine($"New Filled shape1 {shape1.isFilled()}");
        Console.WriteLine($"shape1 to string: {shape1.toString()}");
    }
}