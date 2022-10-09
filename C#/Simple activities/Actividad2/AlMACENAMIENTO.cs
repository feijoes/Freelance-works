using System;

namespace PruebaCalseAbstracta
{
    abstract class ALMACENAMIENTO
    {
        public string Capacidad;
        public string EspacioOcupado;

        public abstract void Escritura();
        public abstract void Lectura();

        public ALMACENAMIENTO()
        {

        }

        public string getCapacidad()
        {
            return this.Capacidad;
        }
        public void setCapacidad(string capacidad)
        {
            this.Capacidad =capacidad;
        }
        public string getEspacioOcupado()
        {
            return this.EspacioOcupado;
        }
        public void setEspacioOcupado(string espacioOcupado)
        {
            this.EspacioOcupado =espacioOcupado;
        }
    }
}