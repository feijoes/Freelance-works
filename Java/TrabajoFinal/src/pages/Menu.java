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

public class Menu extends JFrame {

    Menu()
    {
        this.setTitle("Menu");
        this.setResizable(false);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(null);
        this.add(new MyLabel("     Menu     ",180,10,20));
        JButton nuevopaciente =new JButton("Adicionar Paciente");
        nuevopaciente.setLocation(110, 350);
        nuevopaciente.setSize(150,40);
        nuevopaciente.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent e) {
                setVisible(false);
                dispose();
                PrincipalPage.frame1();
            }
        });
        nuevopaciente.setVisible(true);

        
        JLabel jl = new JLabel();



        
        jl.setSize(200,200);
        jl.setLocation(120, 120);
        jl.setVisible(true);


        BufferedImage img = null;
        try {
            img = ImageIO.read(new File("menu.jpeg"));
        } catch (IOException e) {
            e.printStackTrace();
        }
        Image dimg = img.getScaledInstance(jl.getWidth(), jl.getHeight(),
                Image.SCALE_SMOOTH);
        ImageIcon photo = new ImageIcon(dimg);

        jl.setIcon(photo);

        this.add(jl);

       
        this.add(nuevopaciente);
        this.setSize(500, 500);
        this.setVisible(true);
        this.repaint();
        this.setLocationRelativeTo(null);
    }


}
