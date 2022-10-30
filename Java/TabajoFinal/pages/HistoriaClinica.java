package pages;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class HistoriaClinica extends JFrame {
    
    public HistoriaClinica()
    {
        this.setSize(900, 400);
        this.setResizable(false);
        this.setLocationRelativeTo(null);

        JLabel titulo =  new JLabel("OI");
        this.setLayout(null);
        titulo.setLocation(10, 10);
        this.add(titulo);
    
        
        this.setVisible(true);
    }

    
} 