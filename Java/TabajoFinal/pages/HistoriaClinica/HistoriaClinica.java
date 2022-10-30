package pages.HistoriaClinica;

import javax.swing.JButton;
import javax.swing.JFrame;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import java.util.HashMap;
import java.util.Map;

import components.MyJTextField.MyJTextField;
import components.MyLabel.MyLabel;
import pages.PrincipalPage;
public class HistoriaClinica extends JFrame {
    final int SCREEN_WIDTH = 1000;
    final int SCREEN_HEIGHT =500;
    final int fontsize = 13;
    HistoriaClinica frame = this;
    Map<String, String> dictInputs = new HashMap<String, String>();
    public HistoriaClinica()
    {
        
        this.setTitle("Historia clinica del paciente");
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(null);
        
        this.addLabels();
        this.addInputs();
        
        JButton continuar =new JButton("Continuar");
        continuar.setLocation(600, 350);
        continuar.setSize(100,40);
        continuar.addActionListener(new ActionListener(){  
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.setVisible(false);
                frame.dispose();
                PrincipalPage.frame2(dictInputs); 
            }  
        });  
        continuar.setVisible(true);
        this.add(continuar);


        
        this.setSize(SCREEN_WIDTH, SCREEN_HEIGHT);
        this.setVisible(true);
        this.repaint();
        this.setLocationRelativeTo(null);
    }

    public void addLabels()
    {
        this.add(new MyLabel("1Dados Generales", 5, 5,fontsize));
        this.add(new MyLabel("Nombre del paciente:",15, 30,fontsize));
        this.add(new MyLabel("HISTORIA CLINICA DE UN PACIENTE",400, 0,fontsize));
        this.add(new MyLabel("Fecha de Nacimiento:",420, 30,fontsize));
        this.add(new MyLabel("Edad:",700, 30,fontsize));
        this.add(new MyLabel("Sexo:",830, 30,fontsize));
        this.add(new MyLabel("Eps:",300, 70,fontsize));
        this.add(new MyLabel("Fecha de ingreso:",520, 70,fontsize));
        this.add(new MyLabel("4 Antecedentes",3, 100,fontsize));
        this.add(new MyLabel("Antecedentes Personales:",13, 127,fontsize));
        this.add(new MyLabel("Antecedentes Familiares:",500, 127,fontsize));
        this.add(new MyLabel("2 Motivo Consulta:",3, 290,fontsize));
        this.add(new MyLabel("3 Enfermedad Actual:",3, 330,fontsize));
        this.add(new MyLabel("5 Examen Fisico:",3, 370,fontsize));

    }
    public void addInputs()
    {
        addInput(new MyJTextField(270,17,135,35, "NombrePaciente",dictInputs));
        addInput(new MyJTextField(150,17, 545, 35, "FechaNacimiento",dictInputs));
        addInput(new MyJTextField(90,17, 735, 33, "Edad",dictInputs));
        addInput(new MyJTextField(90,17, 870, 33, "Sexo",dictInputs));
        addInput(new MyJTextField(180,17, 330, 73, "Eps",dictInputs));
        addInput(new MyJTextField(130,17, 625, 73, "FechaIngreso",dictInputs));
        addInput(new MyJTextField(200,17, 110, 300, "MotivoConsulta",dictInputs));
        addInput(new MyJTextField(300,17, 130, 335, "EnfermedadActual",dictInputs));
        addInput(new MyJTextField(250,17, 110, 370, "ExamenFisico",dictInputs));
    }
    public void addInput(MyJTextField input)
    {
        dictInputs.put(input.Name, "");
        this.add(input);
    }

    
} 