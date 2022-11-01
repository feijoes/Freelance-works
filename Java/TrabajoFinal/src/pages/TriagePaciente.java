package pages;

import javax.swing.JButton;
import javax.swing.JFrame;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import components.MyJTextField;
import components.MyLabel;
import components.MyRadioButton;
import controllers.MainController;

public class TriagePaciente extends JFrame {
    final int SCREEN_WIDTH = 1000;
    final int SCREEN_HEIGHT =500;
    final int fontsize = 13;

    Map<String, String> dictInputs = new HashMap<String, String>();
    public TriagePaciente()
    {


        this.setTitle("Triage Paciente");
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(null);
        this.addLabels();
        this.addInputs();
        JButton continuar =new JButton("Confirmar");
        continuar.setLocation(600, 350);
        continuar.setSize(100,40);
        continuar.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                try {
                    MainController.saveinfo(dictInputs);
                } catch (IOException ex) {
                    throw new RuntimeException(ex);
                }
            }
        });
        continuar.setVisible(true);
        this.add(continuar);

        this.setSize(SCREEN_WIDTH, SCREEN_HEIGHT);
        this.setVisible(true);
        this.repaint();
        this.setLocationRelativeTo(null);
    }
    public void saveData(){

    }
    public void addLabels()
    {
        this.add(new MyLabel("Indique su temperatura:", 53, 15,fontsize));
        this.add(new MyLabel("Fiebre:", 5, 30,fontsize));
        this.add(new MyLabel("Tos:", 5, 70,fontsize));
        this.add(new MyLabel("Odinofagia:", 8, 110,fontsize));
        this.add(new MyLabel("Dificultad para respirar:", 8, 200,fontsize));
        this.add(new MyLabel("Cefalea:", 8, 260,fontsize));
        this.add(new MyLabel("Taquicardia/Bradicardia:", 8, 335,fontsize));
        this.add(new MyLabel("Tipertension Arterial/Hipotension:", 180, 390,fontsize));
        this.add(new MyLabel("Saturacion de Oxigeno:", 500, 35,fontsize));
        this.add(new MyLabel("Triage de un Paciente:", 430, 5,fontsize+5));
        this.add(new MyLabel("Antecedentes Familiares:",500, 127,fontsize));
    }
    public void addInputs()
    {
        addInput(new MyJTextField(150,17, 650, 127, "AntecedentesFamiliares",dictInputs));
        addInput(new MyJTextField(130,17,53,33, "Fiebre",dictInputs));


        addInput(new MyRadioButton(48,46,"Tos",dictInputs));
        addInput(new MyRadioButton(70,95,"Odinofagia",dictInputs));
        addInput(new MyRadioButton(110, 180,"Dificultad_respirar",dictInputs));
        addInput(new MyRadioButton(50, 240,"Cefalea",dictInputs));
        addInput(new MyRadioButton(135, 315,"Taquicardia/Bradicardia","Taquicardia","Bradicardia",dictInputs));
        addInput(new MyRadioButton(350, 350,"Tipertension Arterial/Hipotension","Tipertension Arterial","Hipotension",dictInputs));
        addInput(new MyJTextField(130,17,640,37,"satu",dictInputs));

    }
    public void addInput(MyJTextField input)
    {
        dictInputs.put(input.Name, "");
        this.add(input);
    }
    public void addInput(MyRadioButton input)
    {
        dictInputs.put(input.name,input.getType());
        this.add(input);
    }


} 