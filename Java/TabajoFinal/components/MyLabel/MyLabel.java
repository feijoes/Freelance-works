package components.MyLabel;

import java.awt.Dimension;
import java.awt.Font;

import javax.swing.JLabel;

public class MyLabel  extends JLabel{
    
    public MyLabel(String text,int x,int y, int fontsize)
    {
        setText(text);
       
        setFont(new Font(getFont().getFamily(), Font.PLAIN, fontsize));
        Dimension size = this.getPreferredSize();
        setSize((int)size.getWidth(), (int) size.getHeight());
        setLocation(x, y);
        setVisible(true);
        
    }
}