using System;
namespace Empresa
{
    public class EmpleadoProduccion : Asalariado
    {
        string Turno;

        public EmpleadoProduccion(): base(){
            Turno = "";
        }

        public EmpleadoProduccion(string nombre,string apellido, int codigo, int salario,string turno): base(nombre,apellido,codigo,salario)
        {
            this.Turno = turno;
        }

        public string getTurno()
        {
            return this.Turno;
        }
        public void setTurno(string turno)
        {
            this.Turno = turno;
        }

    }
}