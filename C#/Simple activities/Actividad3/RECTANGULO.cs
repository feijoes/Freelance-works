using System;

namespace PruebaInterfaz2
{
    class RECTANGULO: IPARARELOGRAMO
    {
        public int Base;
        public int Altura;

        public RECTANGULO()
        {
            Base=0;
            Altura=0;
        }
        public RECTANGULO(int Base, int Altura)
        {
            this.Base=Base;
            this.Altura=Altura;
        }
        public int getBase()
        {
            return this.Base;
        }
        public void setBase(int Base)
        {
            this.Base = Base;
        }
        public int getAltura()
        {
            return this.Altura;
        }
        public void setAltura(int Altura)
        {
            this.Altura = Altura;
        }

        public int CALCULARAREA()
        {
            return Altura*Base;
        }
        public double CALCULARPERIMETRO()
        {
            return (2*Altura)+(2*Base);
        }
    }
}