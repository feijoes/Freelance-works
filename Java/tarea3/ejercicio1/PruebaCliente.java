public class PruebaCliente {

    public static void main(String[] args) {
    // Declarar dos instancias de la clase Cliente
    Cliente cliente1 = new Cliente();
    Cliente cliente2 = new Cliente();

    // Asignar valores a las variables miembro de la instancia Cliente.
    cliente1.clienteID = 1111;
    cliente1.nombre = "Juan Perez";
    cliente1.email = "juan.perez@example.com";

    cliente2.clienteID = 2222;
    cliente2.nombre = "Maria Garcia";
    cliente2.email = "maria.garcia@example.com";

    // Asignar una variable de referencia a objetos a otra variable de referencia a objetos
    Cliente cliente3 = cliente1;

    // Invocar el método muestraClienteInfo() para cada uno de los Objetos Cliente.
    cliente1.muestraClienteInfo();
    cliente2.muestraClienteInfo();
    cliente3.muestraClienteInfo();
  }
} // fin de la clase