using System;
namespace Empresa
{
    public class EmpleadoDistribucion: Asalariado
    {
        string Zona;

        public EmpleadoDistribucion(): base(){
            Zona = "";
        }

        public EmpleadoDistribucion(string nombre,string apellido, int codigo, int salario,string zona): base(nombre,apellido,codigo,salario)
        {
            this.Zona = zona;
        }

        public string getZona()
        {
            return this.Zona;
        }
        public void setZona(string zona)
        {
            this.Zona = zona;
        }

    }
}