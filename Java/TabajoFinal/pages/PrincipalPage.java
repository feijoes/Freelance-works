package pages;

import java.util.HashMap;
import java.util.Map;

import pages.HistoriaClinica.HistoriaClinica;
import pages.TriagePaciente.TriagePaciente;

public class PrincipalPage {
    
    public PrincipalPage()
    {
        new TriagePaciente(new HashMap<>());
        //new HistoriaClinica();
    }

    public static void frame2(Map<String,String> dictInputs)
    {
        new TriagePaciente(dictInputs);    
    }
}
