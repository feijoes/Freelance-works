using System;
namespace Ejercicio1
{
    public class Persona
    {
        string Apellido;
        string Nombre;
        int Telefono;
        Auto? auto;
        public Persona(string Apellido,string Nombre,int Telefono)
        {
            this.Apellido = Apellido;
            this.Nombre = Nombre;
            this.Telefono = Telefono;
        }

        public void NuevoAuto(Auto auto) => this.auto = auto;
        public void Operation1() => Console.WriteLine("?");
    }
}