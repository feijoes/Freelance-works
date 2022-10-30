package pages.TriagePaciente;

import javax.swing.JButton;
import javax.swing.JFrame;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import java.util.Map;

import components.MyJTextField.MyJTextField;
import components.MyLabel.MyLabel;
import pages.PrincipalPage;



public class TriagePaciente extends JFrame {
    final int SCREEN_WIDTH = 1000;
    final int SCREEN_HEIGHT =500;
    final int fontsize = 13;

    Map<String, String> dictInputs;
    public TriagePaciente(Map<String, String> inputs)
    {
        dictInputs = inputs;
        
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
                System.out.println("Test ");
                
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
        this.add(new MyLabel("Indique su temperatura: jdscods udsaidjsa 9dnids", 0, 100,fontsize));
        this.add(new MyLabel("Fiebre jdjifkdjs ijdsikdfs", 5, 50,fontsize));
    }
    public void addInputs()
    {
        addInput(new MyJTextField(270,17,135,35, "NombrePaciente",dictInputs));
    }
    public void addInput(MyJTextField input)
    {
        dictInputs.put(input.Name, "");
        this.add(input);
    }

    
} 