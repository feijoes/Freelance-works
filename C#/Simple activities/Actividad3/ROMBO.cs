using System;

namespace PruebaInterfaz2
{
    class ROMBO: IPARARELOGRAMO
    {
        public int DiagonalMayor;
        public int DiagonalMenor;

        public ROMBO()
        {
            DiagonalMayor=0;
            DiagonalMenor=0;
        }
        public ROMBO(int DiagonalMayor, int DiagonalMenor)
        {
            this.DiagonalMayor=DiagonalMayor;
            this.DiagonalMenor=DiagonalMenor;
        }
        public int getDiagonalMayor()
        {
            return this.DiagonalMayor;
        }
        public void setDiagonalMayor(int DiagonalMayor)
        {
            this.DiagonalMayor = DiagonalMayor;
        }
        public int getDiagonalMenor()
        {
            return this.DiagonalMenor;
        }
        public void setDiagonalMenor(int DiagonalMenor)
        {
            this.DiagonalMenor = DiagonalMenor;
        }

        public int CALCULARAREA()
        {
            return (DiagonalMenor*DiagonalMayor)/2;
        }
        public double CALCULARPERIMETRO()
        {
            return Math.Sqrt(Math.Pow(DiagonalMayor,2)+Math.Pow(DiagonalMenor,2))*2;
        }
    }
}