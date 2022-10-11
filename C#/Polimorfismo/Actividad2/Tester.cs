namespace Polimorfismo.Actividade2
{
    internal partial class Tester
    {
        private static void Main(string[] args)
        {
            Licenciado L = new Licenciado();
            L.tipogrado();
            Inginerio I = new Inginerio();
            I.tipogrado();
        }
    }
}
// tuve que usar Polimorfismo de Sobrecarga