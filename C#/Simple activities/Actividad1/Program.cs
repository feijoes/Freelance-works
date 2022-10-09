using Empresa;
internal class Program
{
    private static void Main(string[] args)
    {
        EmpleadoProduccion empleadoProduccion = new EmpleadoProduccion();
        Console.WriteLine(empleadoProduccion.getCodigo());
        empleadoProduccion.setApellido("Nuevo appellido");
        Console.WriteLine(empleadoProduccion.getApellido());

        EmpleadoDistribucion empleadoDistribucion = new EmpleadoDistribucion("Pedro","Ramires",3,2,"test zona");

        Console.WriteLine(empleadoDistribucion.getZona());
        Console.WriteLine(empleadoDistribucion.getCodigo());

    }
}