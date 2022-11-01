package pages;


import components.MyLabel;
import controllers.MainController;
import javax.swing.*;
import java.io.IOException;
import java.util.ArrayList;


public class Pacientes extends JFrame {
    final int SCREEN_WIDTH = 400;
    final int SCREEN_HEIGHT =400;

    public ArrayList info;


    Pacientes() {

        try {
            this.info = MainController.getInfo();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        this.setTitle("Pacientes");
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

        this.add(new MyLabel("LOS PACIENTES QUE INGRESARON A URGENCIA FUERON TANTO: ",10,12,12));
        this.add(new MyLabel("SE FUERON PARA LA CASA: " + this.info.get(0),20,100,12));
        this.add(new MyLabel("EN OBSERVACION SE ENCUENTRAN: "+ this.info.get(1),20,120,12));
        this.add(new MyLabel("EN HOSPILITACION SE ENCUETRAN: "+ this.info.get(2),20,140,12));
        this.add(new MyLabel("A UCI LLEGARAN: "+ this.info.get(3),20,160,12));
    }

}
