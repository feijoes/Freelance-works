using System.Collections.Generic;
using System;
namespace Ejercicio3
{
    public class Ciudad
    {
        int Codigo_Postal;
        string Nombre;
        int Prefijo_telefonico;
        Provincia provincia;

        List<Persona> Personas = new List<Persona>();

        public Ciudad(int Codigo_Postal, string Nombre, int prefijo_telefonico,  Provincia provincia)
        {
            this.Codigo_Postal = Codigo_Postal;
            this.Nombre = Nombre;
            this.Prefijo_telefonico = prefijo_telefonico;
            this.provincia = provincia;  
        }
        public int DevolverNumeroMasPrefijo(int Telefono) => Convert.ToInt32($"{Prefijo_telefonico}{Telefono}");
        public void AdicionarPersona(Persona persona)
        {
            Personas.Add(persona);
        }
        public List<Persona> MostrarPersonas()
        {
            return Personas;
        }


























    }
}