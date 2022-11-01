package components;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Map;

public class MyRadioButton extends JPanel {
    public String name;
    ButtonGroup group;

    String select = "no";

    Map<String,String> dictInputs;
    ActionListener listener = new ActionListener() {

        @Override
        public void actionPerformed(ActionEvent e) {
            dictInputs.put(name, e.getActionCommand());
        }
    };

    public MyRadioButton(int x, int y,String name,Map<String,String> dictInputs){
        this.dictInputs = dictInputs;
        this.name = name;
        JRadioButton si = new JRadioButton("si",false);
        JRadioButton no = new JRadioButton("no",true);
        si.addActionListener(listener);
        no.addActionListener(listener);

        this.group = new ButtonGroup();
        this.group.add(si);
        this.group.add(no);
        this.setAlignmentX(x);
        this.setAlignmentY(y);
        this.setSize(50,60);
        this.add(si);
        this.add(no);
        this.setLocation(x,y);
        this.setVisible(true);
    }
    public MyRadioButton(int x, int y, String name, String op1, String op2, Map<String,String> dictInputs){
        this.dictInputs =dictInputs;
        this.name = name;
        JRadioButton si = new JRadioButton(op1,false);
        JRadioButton no = new JRadioButton(op2,false);
        JRadioButton nada = new JRadioButton("no",true);


        si.addActionListener(listener);
        no.addActionListener(listener);
        nada.addActionListener(listener);
        this.group = new ButtonGroup();
        this.group.add(si);
        this.group.add(no);
        this.group.add(nada);
        this.setSize(140,110);
        this.add(si);
        this.add(no);
        this.add(nada);
        this.setLocation(x,y);
        this.setVisible(true);
    }
    public String getType(){
        return select;
    }

}
