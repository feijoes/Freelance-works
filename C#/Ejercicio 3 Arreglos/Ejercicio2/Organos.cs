
namespace Ejercicio2
{
    public class Organo
    {
        string Funcion;
        string Nombre;
       
        public Organo(string Funcion,string Nombre)
        {
            this.Funcion = Funcion;
            this.Nombre = Nombre;
        }
        public void Funcionar()
        {
            Console.WriteLine($"{Nombre} esta funcionando");
        }
    }
}