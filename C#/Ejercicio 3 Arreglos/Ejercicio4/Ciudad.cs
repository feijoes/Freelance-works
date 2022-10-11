using System;
using System.Collections.Generic;
namespace Ejercicio4
{
    public class Ciudad
    {
        int Codigo_Postal;
        string Nombre;
        int Prefijo_telefonico;

        List<Persona> Personas = new List<Persona>();

        public Ciudad(int Codigo_Postal, string Nombre, int prefijo_telefonico)
        {
            this.Codigo_Postal = Codigo_Postal;
            this.Nombre = Nombre;
            this.Prefijo_telefonico = prefijo_telefonico;  
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