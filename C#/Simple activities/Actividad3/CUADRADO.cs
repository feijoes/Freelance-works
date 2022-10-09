using System;

namespace PruebaInterfaz2
{
    class CUADRADO: IPARARELOGRAMO
    {
        public int Lado;
        public CUADRADO()
        {
            Lado=0;
        }
        public CUADRADO(int lado)
        {
            this.Lado = lado;
        }
        public int getLado()
        {
            return this.Lado;
        }
        public void setLado(int Lado)
        {
            this.Lado = Lado;
        }

        public int CALCULARAREA()
        {
            return Lado*Lado;
        }
        public double CALCULARPERIMETRO()
        {
            return Lado*4;
        }
    }
}