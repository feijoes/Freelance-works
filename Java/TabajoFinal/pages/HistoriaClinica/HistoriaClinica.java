package pages.HistoriaClinica;

import javax.swing.JFrame;

import components.MyLabel;
public class HistoriaClinica extends JFrame {
    final int SCREEN_WIDTH = 1000;
    final int SCREEN_HEIGHT =500;
    final int fontsize = 13;
    public HistoriaClinica()
    {
        this.setTitle("Historia clinica del paciente");
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(null);
        
        this.addLabels();




        
        this.setSize(SCREEN_WIDTH, SCREEN_HEIGHT);
       
        this.setVisible(true);
        this.repaint();
        this.setLocationRelativeTo(null);
    }

    public void addLabels()
    {
        this.add(new MyLabel("1Dados Generales", 5, 5,fontsize));
        this.add(new MyLabel("Nombre del paciente",15, 30,fontsize));
        this.add(new MyLabel("HISTORIA CLINICA DE UN PACIENTE",400, 0,fontsize));
        this.add(new MyLabel("Fecha de Nacimiento",420, 30,fontsize));
        this.add(new MyLabel("Edad",700, 30,fontsize));
        this.add(new MyLabel("Sexo",830, 30,fontsize));
        this.add(new MyLabel("Eps",300, 70,fontsize));
        this.add(new MyLabel("Fecha de ingreso",520, 70,fontsize));
        this.add(new MyLabel("4 Antecedentes",3, 100,fontsize));
        this.add(new MyLabel("Antecedentes Personales",13, 127,fontsize));
        this.add(new MyLabel("Antecedentes Familiares",500, 127,fontsize));
        this.add(new MyLabel("2 Motivo Consulta",3, 290,fontsize));
        this.add(new MyLabel("3 Enfermedad Actual",3, 330,fontsize));
        this.add(new MyLabel("5 Examen Fisico",3, 370,fontsize));

    }

    
} 