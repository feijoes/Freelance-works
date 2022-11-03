package pages;



public class PrincipalPage {

    public PrincipalPage()
    {
        new Bienvenido();
    }
    public static void frame0(){ new Menu();}
    public static void frame1(){ new HistoriaClinica();}
    public static void frame2()
    {
        new TriagePaciente();
    }

    public static  void frame3() {new Pacientes(); }
}
