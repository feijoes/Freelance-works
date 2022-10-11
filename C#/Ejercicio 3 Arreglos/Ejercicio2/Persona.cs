
namespace Ejercicio2
{
    public class Persona
    {
        string Apellido;
        string Nombre;
        int Telefono;

        List<Organo> Organos = new List<Organo>();
        public Persona(string Apellido,string Nombre,int Telefono, List<Organo> organos)
        {
            this.Apellido = Apellido;
            this.Nombre = Nombre;
            this.Telefono = Telefono;
            this.Organos =organos;
        }
        public void Operation1()
        {
            Console.WriteLine("?");
        }
        public void FuncionarOrganos()
        {
            foreach( Organo organo in  Organos)
            {
                organo.Funcionar();
            }
        }
    }
}