using System;

namespace PruebaCalseAbstracta
{
    class MEMORIAUSB : ALMACENAMIENTO
    {
        public MEMORIAUSB()
        {
            this.Capacidad = "50Gb";
            this.EspacioOcupado = "15Gb";
        }
        public override void Lectura()
        {
            Console.WriteLine("Se esta leyendo la memoria USB");
        }
        public override void Escritura()
        {
            Console.WriteLine("Se esta grabando la memoria USB");
        }
    }

}