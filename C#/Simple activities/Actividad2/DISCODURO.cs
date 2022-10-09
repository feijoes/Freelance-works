
using System.Runtime.InteropServices.ComTypes;
using System;

namespace PruebaCalseAbstracta
{
    class DISCODURO : ALMACENAMIENTO
    {
        public DISCODURO()
        {
            this.Capacidad="500Gb";
            this.EspacioOcupado="100Gb";
        }
        public override void Lectura()
        {
            Console.WriteLine("Se esta leyendo en el Disco duro");
        }
        public override void Escritura()
        {
            Console.WriteLine("Se esta grabando en el Disco duro");
        }

    }
}