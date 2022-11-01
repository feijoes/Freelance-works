package components;

import java.awt.Dimension;
import java.awt.Font;

import javax.swing.JLabel;

public class MyLabel  extends JLabel{

    public MyLabel(String text,int x,int y, int fontsize)
    {
        this.setText(text);

        this.setFont(new Font(getFont().getFamily(), Font.PLAIN, fontsize));
        Dimension size = this.getPreferredSize();
        this.setSize((int)size.getWidth(), (int) size.getHeight());
        this.setLocation(x, y);
        this.setVisible(true);

    }
}