using Ejercicio1;
public class ShirtArrayTest {
    public static void Main(string[] args) {
        Shirt [] ShirtsArray = new Shirt[3];

        Shirt myShirt1 = new Shirt(101, "Camisa Roja", 'R', 45.20, 10);
        Shirt myShirt2 = new Shirt(202, "Camisa Azul", 'B', 60.32, 12);
        Shirt myShirt3 = new Shirt(303, "Camisa Verde", 'G', 19.02, 5);

        ShirtsArray[0] = myShirt1;
        ShirtsArray[1] = myShirt2;
        ShirtsArray[2] = myShirt3;

        for(int i=0; i<ShirtsArray.Length; i++){
            ShirtsArray[i].displayInformation();
        }
    }
}