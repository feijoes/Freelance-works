import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) {




        List<Integer> lista = new JULinkedList();
        System.out.println(lista.isEmpty());

        lista.add(1);
        lista.add(2);
        lista.add(3);

        System.out.println(lista.size());

        lista.remove(1);
        System.out.println(lista.size());

        System.out.println(lista.isEmpty());

        System.out.println("-------String List -------------");

        List<String> lista2 = new JULinkedList();
        System.out.println(lista2.isEmpty());

        lista2.add("1");
        lista2.add("2");
        lista2.add("3");

        System.out.println(lista2.size());

        lista2.remove("1");
        lista2.get(0);
        System.out.println(lista2.contains("3"));
        System.out.println(lista2.size());

        System.out.println(lista2.isEmpty());


    }
}