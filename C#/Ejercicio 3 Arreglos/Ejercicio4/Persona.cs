using System;
namespace Ejercicio4
{
    public class Persona
    {
        string Apellido;
        string Nombre;
        int Telefono;

        Ciudad ciudad;
        public Persona(string Apellido,string Nombre,int Telefono, Ciudad ciudad)
        {
            this.Apellido = Apellido;
            this.Nombre = Nombre;
            this.Telefono = Telefono;
            this.ciudad = ciudad;
        }
        public void Operation1()
        {
            Console.WriteLine("?");
        }
    }
}