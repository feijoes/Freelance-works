using System;
namespace Empresa
{
    public class Asalariado
    {
        string Nombre;
        string Apellido;
        int Salario;
        int Codigo;
        public Asalariado()
        {
            Nombre ="";
            Apellido="";
            Salario =0;
            Codigo = 0;
        }
        public Asalariado(string nombre,string apellido, int codigo, int salario)
        {
            this.Apellido = apellido;
            this.Codigo = codigo;
            this.Nombre = nombre;
            this.Salario = salario;
        }
        public string getNombre()
        {
            return this.Nombre;
        }
        public void setNombre(string nombre)
        {
            this.Nombre = nombre;
        }
        public string getApellido()
        {
            return this.Apellido;
        }
        public void setApellido(string apellido)
        {
            this.Apellido = apellido;
        }
        public int getCodigo()
        {
            return this.Codigo;
        }
        public void setCodigo(int codigo)
        {
            this.Codigo = codigo;
        }
        public int getSalario()
        {
            return this.Salario;
        }
        public void setSalario(int salario){
            this.Salario = salario;
        } 

    } 
}