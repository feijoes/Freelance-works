import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {




        List<Integer> lista = new JULinkedList();
        System.out.println(lista.isEmpty());

        lista.add(1);
        lista.add(2);

        System.out.println(lista.size());
        System.out.println(lista.isEmpty());


    }
}