/*
 * Tarea(individual) para agosto 30, Enviar MR hasta 8AM, usando únicamente su estructura `Stack` implementada en su tarea anterior. Implementar una solución que permita realizar cálculos aritméticos dada una cadena de entrada, todos los operandos son números enteros(int) positivos, y la respuesta también debe ser un numero entero. Cada evaluación debe hacerse de izquierda a derecha, además de respetar la prioridad de operadores, para los siguientes (ordenados de mayor a menor prioridad):

! (factorial)
^ (potencia)
+ (suma)
* (multiplicación)
Nótese que para esta tarea la multiplicación tiene menor prioridad que la suma.

Ejemplos base:

“1+2+3” => 6

“2*2*5” => 20

“2^3+2” => 10

“1+2*5” => 15

“5! + 10” => 130

“3!^2” => 36

“4^2*3” => 24

“3^3!+5*2” => 1468

Como segunda parte: la prioridad de operadores puede cambiarse con el uso de paréntesis:

“(1+2)+3” => 6

“2*(2*5)” => 20

“(2^3)+2” => 10

“2^(3+2)” => 64

“(1+2)*5” => 15

“1+(2*5)” => 11

“!(3 + 2)” => 120

“(3!)^2” => 36

“4^(2*3)” => 4096

“3^3!+(5*2)” => 739

 

 

De la evaluación:

- Aplicar POO.

- Ningún método puede pasar de las 20 líneas de código, además de mantener la legibilidad (de ser necesario llevar la lógica a otro método)

- Se evaluará cada hito alcanzado, desde lo más básico, pasando por la mescla de operadores de distinta prioridad, hasta el manejo paréntesis que cambien la prioridad de operadores. Cada hito se evalúa desde las pruebas unitarias descritas más adelante.

- la cadena de entrada que sea invalida por algún motivo, debe responder con una clase Exception propia, es decir por ejemplo si contiene algún carácter que no pertenece ni a los operadores descritos ni aun número entero, se debe indicar en la Excpetion específica, cual ese carácter. Otro posible problema será cuando un conjunto de combinaciones no sea una entrada valida, como: “2*”, “2*2”, “3+6^”, “1+1!”, etc, se debe responder con su respectiva Excpetion. Otro posible problema será cuando la respuesta este fuera de los limites de un numero entero: “!1000”

- Cada infracción puede quitar puntos según su peso.

 

Restricciones:

- Solo se puede usar como estructura la clase `Stack` que Uds. mismos implementaron en la tarea anterior, dejando de lado cualquier otra estructura de datos, incluidos los arreglos. La infracción de esta restricción puede invalidar la tarea por completo.

- Toda lógica usada en esta solución debe ser implementada por Uds. mismos. Lo que también significa que no se pueden usar métodos, servicios, ni algoritmos de terceros ni los provistos por el lenguaje como ser los de las librerías `Arrays` , `Collections`, ni otros.

- No se puede usar la clase `StringBuilder`
- No se puede usar la clase `StringBuffer`
- No se puede usar la clase `String` salvo algunos particulares, ejemplo: los mensajes de las excepciones, que implementen, al momento de formar los operandos: 

`

Character c1 = '1';

Character c2 = '2';

int num = Integer.parseInt(c1 + "" + c2);

`

Nota: que los operandos pueden tener más de un digito.

Para llevar la cadena de entrada a su estructura pueden usar este método:

`
public static Stack<Character> getTokens(String str) {

    Stack<Character> tokens = new Stack<>();

    for (int i = 0; i < str.length(); i++) {

        tokens.push(str.charAt(i));

    }

 

    return tokens;

}

`
, luego se puede negociar otras necesidades para la clase `String`


- Ningún método puede pasar de las 20 líneas de código


Pruebas unitarias:

Para las pruebas unitarias cada operador debe tener sus propias pruebas (que pueden estar separadas en sus propias clases test), luego diferentes combinaciones entre operadores de distinta prioridad, primero solo 2 operadores de distinta prioridad y en siguientes pruebas añadiendo más operadores.
Toda clase/método implementado debe tener sus propias pruebas unitarias.
 */

import java.util.Stack;

/*
! (factorial)
^ (potencia)
+ (suma)
* (multiplicación)
 */
class Solution {

  public static int value(int num, Stack<Character> stack) {
    return num;
  }

  public static int getIndex(String s) {
    int n = s.length();
    int oneMore = 0;

    for (int i = 0; i < n; i++) {
      char curr = s.charAt(i);
      switch (curr) {
        case '(':
          oneMore++;
          break;
        case ')':
          if (oneMore == 0) {
            
            return i+1;
          } else {
            oneMore--;
          }
          break;
      }
    }
    return n;
  }

  public static String calculate(String s) {
    Stack<Character> stackant = new Stack<Character>();
    String news = "";
    int sing=0;
    for (int i=0; i < s.length();i++){

      if (s.charAt(i) == '('){
        calculate(s.substring(i+1, getIndex(s.substring(i+1))));
      }
      if (s.charAt(i) == '^'){
        int before =1;
        int next=1;
        while (i+next < s.length()){
          if (Character.isDigit(s.charAt(i + next))){next++;}
          else{break;}
         
        }
        while (Character.isDigit(s.charAt(i -before))){
          before--;
        }
        news = s.replace(s.substring(before,next+1), ""+(int)Math.pow(Integer.parseInt(s.substring(before,i)), Integer.parseInt(s.substring(before,i))));
      }
      if(s.charAt(i) == '!'){
        sing=3;
      }
      
      
    }
    return news;
  }
}

public class Main {

  public static void main(String args[]) {
    System.out.println(Solution.calculate("10^4 "));
  }
}
