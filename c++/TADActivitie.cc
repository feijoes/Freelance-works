#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <cctype>
#include <map>

class ExpresionStack {
public:
    ExpresionStack();
    bool compilarExpresion(const std::string& expresion);
    double resultado();

private:
    std::stack<char> operators;
    std::vector<double> values;

    // Función para obtener la precedencia de un operador
    int obtenerPrecedencia(char operador);

    // Función para evaluar y aplicar operadores
    void aplicarOperador();
};

ExpresionStack::ExpresionStack() {}

bool ExpresionStack::compilarExpresion(const std::string& expresion) {
    std::map<char, int> precedencia;
    precedencia['+'] = 1;
    precedencia['-'] = 1;
    precedencia['*'] = 2;
    precedencia['/'] = 2;

    for (char c : expresion) {
        if (std::isdigit(c)) {
            double valor = c - '0';
            values.push_back(valor);
        } else if (c == '(') {
            operators.push(c);
        } else if (c == ')') {
            while (!operators.empty() && operators.top() != '(') {
                aplicarOperador();
            }
            operators.pop();  // Elimina el paréntesis izquierdo
        } else if (c == '+' || c == '-' || c == '*' || c == '/') {
            while (!operators.empty() && precedencia[c] <= precedencia[operators.top()]) {
                aplicarOperador();
            }
            operators.push(c);
        }
    }

    while (!operators.empty()) {
        aplicarOperador();
    }

    return true;
}

double ExpresionStack::resultado() {
    if (values.size() == 1 && operators.empty()) {
        return values[0];
    } else {
        std::cerr << "Expresión inválida" << std::endl;
        return 0;
    }
}

int ExpresionStack::obtenerPrecedencia(char operador) {
    std::map<char, int> precedencia;
    precedencia['+'] = 1;
    precedencia['-'] = 1;
    precedencia['*'] = 2;
    precedencia['/'] = 2;
    return precedencia[operador];
}

void ExpresionStack::aplicarOperador() {
    if (values.size() < 2 || operators.empty()) {
        std::cerr << "Expresión inválida" << std::endl;
        return;
    }

    double operand2 = values.back();
    values.pop_back();

    double operand1 = values.back();
    values.pop_back();

    char operador = operators.top();
    operators.pop();

    double resultado = 0.0;
    switch (operador) {
        case '+':
            resultado = operand1 + operand2;
            break;
        case '-':
            resultado = operand1 - operand2;
            break;
        case '*':
            resultado = operand1 * operand2;
            break;
        case '/':
            resultado = operand1 / operand2;
            break;
    }

    values.push_back(resultado);
}

int main() {
     ExpresionStack expresionStack;
    std::string expresion;

    std::cout << "Enter an expression (e.g., (2+2)*5): ";
    std::cin >> expresion;

    if (expresionStack.compilarExpresion(expresion)) {
        double resultado = expresionStack.resultado();
        std::cout << "Resultado: " << resultado << std::endl;
    }

    return 0;
}