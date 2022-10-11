public class GuessingGame {

    public bool isNumeric(string str){ // COMPROBAR SI EL ARGUMENTO ES UN NUMERO O UN STRING.
        try{
            int value = Convert.ToInt32(int.Parse(str));
            return true;
        }
        catch (Exception){
            return false;
        }
    }
    public static void Main(string[] args) {
        Console.WriteLine(args);
        if(args.Length == 1){
            GuessingGame myGuess = new GuessingGame();

            if(myGuess.isNumeric(args[0])){
                if((int.Parse(args[0]) >= 1) && (int.Parse(args[0]) <= 5)){
                    Random rnd = new Random();


                    int randomNumber = rnd.Next(1,6);
                    if(int.Parse(args[0]) == randomNumber){
                        Console.WriteLine("\nFelicidades!! Ha acertado el numero.");
                    }
                    else{
                        Console.WriteLine("\nTe equivocaste!! Intenta denuevo.");
                        Console.WriteLine("\nEl numero generado fue: " + randomNumber);
                    }
                }
                else{
                    Console.WriteLine("\nERROR!! Debe introducir un numero mayor o igual a 1 y menor o igual a 5.");
                }
            }
            else if(args[0].Equals("help")){
                Console.WriteLine("\n\n\n************************** INSTRUCCIONES **************************");
                Console.WriteLine("\nPrimero: Agregar un numero entre 0 y 6.");
                Console.WriteLine("\nSegundo: Comprobar si el numero coincide.");
            }
            else{
                Console.WriteLine("\nSolo puede agregar numeros mayores o iguales a 1 y menores o iguales a 5 y/0 "
                                    + "la palabra reservada \"help\"");
            }
        }
        else{
            Console.WriteLine("\nDebe agregar un rango valido de argumentos.");
        }
    }
}