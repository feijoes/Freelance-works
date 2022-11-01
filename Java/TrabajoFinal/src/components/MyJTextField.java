package components;
import java.util.Map;

import javax.swing.JTextField;
import javax.swing.event.DocumentEvent;
import javax.swing.event.DocumentListener;
public class MyJTextField extends JTextField{

    public String Name;
    public MyJTextField(int width,int height,int x, int y, String Name, Map<String,String> dict)
    {
        this.Name = Name;
        this.setLocation(x,y);
        this.setSize(width,height);
        this.setVisible(true);
        this.getDocument().addDocumentListener(new DocumentListener() {

            public void warn() {
                dict.put(Name, getText());
            }
            @Override
            public void insertUpdate(DocumentEvent e) {
                warn();

            }
            @Override
            public void removeUpdate(DocumentEvent e) {
                warn();

            }
            @Override
            public void changedUpdate(DocumentEvent e) {
                warn();

            }
        });
    }
}
