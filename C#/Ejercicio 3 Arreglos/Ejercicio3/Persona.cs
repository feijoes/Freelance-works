using System;
namespace Ejercicio3
{
    public class Persona
    {
        string Apellido;
        string Nombre;
        int Telefono;
        public Persona(string Apellido,string Nombre,int Telefono)
        {
            this.Apellido = Apellido;
            this.Nombre = Nombre;
            this.Telefono = Telefono;
        }
        public void Operation1()
        {
            Console.WriteLine("?");
        }
    }
}