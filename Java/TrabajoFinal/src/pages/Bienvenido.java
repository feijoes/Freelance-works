package pages;

import components.MyLabel;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Map;

public class Bienvenido extends JFrame {
    final int SCREEN_WIDTH = 400;
    final int SCREEN_HEIGHT =400;
    Bienvenido()
    {

        this.setTitle("Hospital");
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(null);
        this.addComponents();
        this.setSize(SCREEN_WIDTH, SCREEN_HEIGHT);
        this.setVisible(true);
        this.repaint();
        this.setLocationRelativeTo(null);
    }
    public void addComponents() {
        JLabel jl = new JLabel();



        Dimension size = jl.getPreferredSize();
        jl.setSize(200,200);
        jl.setLocation(100, 120);
        jl.setVisible(true);


        BufferedImage img = null;
        try {
            img = ImageIO.read(new File("first.jpeg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        Image dimg = img.getScaledInstance(jl.getWidth(), jl.getHeight(),
                Image.SCALE_SMOOTH);
        ImageIcon photo = new ImageIcon(dimg);

        jl.setIcon(photo);

        this.add(jl);
        this.add(new MyLabel("Bienvenida a la parte de urgencias del hospital:", 73, 12, 12));
        JButton Menu =new JButton("Ir para el menu");
        Menu.setLocation(110, 70);
        Menu.setSize(150,40);
        Menu.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                setVisible(false);
                dispose();
                PrincipalPage.frame0();
            }
        });
        this.add(Menu);
    }

}
