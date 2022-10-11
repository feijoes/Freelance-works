
namespace Polimorfismo.Actividade1
{
    public class CEDULA
    {
        public void ver(int cedulasinguiones)
        {
            Console.WriteLine($"La cedula es: {cedulasinguiones}");
        }
        public void ver(int serie,int secuencia,int digitoverificador)
        {
            Console.WriteLine($"La cedula es: {serie}{secuencia}{digitoverificador}");
        }
    }
}
// Tuve que usar Polimorfismo de Paramétrico