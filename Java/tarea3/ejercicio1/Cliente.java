public class Cliente {

  public int clienteID = 0; // Valor de ID incial para el cliente
  public String nombre = "-nombre requerido-"; // inicializado
  public String email = "-email requerido-"; // inicializado

  // Este metodo muestra los valores para un articulo
  public void muestraClienteInfo() {
    System.out.println("**Informacionn del Cliente**");
    System.out.println("ID Cliente: " + clienteID);
    System.out.println("Nombre:" + nombre);
    System.out.println("Email: " + email);
    System.out.println("************");
  } // fin metodo muestra
} // fin de la clase