using System;
namespace Ejercicio1
{
    public class Auto
    {
        string Marca;
        int Modelo;
        public Auto(string Marca,int Modelo)
        {
            this.Marca = Marca;
            this.Modelo = Modelo;
        }

        public void Asegurar()
        {
            Console.WriteLine("Asegurar ?");
        }
        
    }
}