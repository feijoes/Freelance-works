#include <iostream>

using namespace std;

int main()
{
    int a, b, c;

    cout << "\nPrimer lado: "; cin >> a;
    cout << "Segundo lado: "; cin >> b;
    cout << "Tercer lado: "; cin >> c;

    if (a == b == c)
        cout << "\nEs un triangulo Equilatero" << endl;
    else if (a == b || a == c || b == c)
        cout << "\nEs un triangulo Isosceles" << endl;
    else
        cout << "\nEs un triangulo Escaleno" << endl;

    return 0;
}


using namespace std;
int main()
{
    int dia, mes;

    cout << "Dia: "; cin >> dia;
    cout << "Mes: "; cin >> mes;

    cout << "\nEl signo del zodiaco es: ";
    if (mes == 1)
    {
        if (dia < 21)
            cout << "Capricornio";
        else
            cout << "Acuario";
    }
    else if (mes == 2)
    {
        if (dia < 20)
            cout << "Acuario";
        else
            cout << "Piscis";
    }

    cout << endl;

    return 0;
}


#include <iostream>
using namespace std;
int main(int argc, char *argv[]) {
	int numero;
	numero = 50;


	for(int i=1; i<=numero; i++){
		cout<<i<<" "<<i*i<<endl;
	}
	return 0;


#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
	int numero;
	int numero2;

	cout<<"INGRESE UN NUMERO: ";
	cin>>numero;
	cout<<"INGRESE NUMERO 2: ";
	cin>>numero2;


	for(int i=1; i<=numero2; i++){
		cout<<numero<<" * "<<i<<" = "<<numero * i<<endl;
	}
	return 0;
}

#include <iostream>

using namespace std;

int main() {
    int x,y;
    char operacion;

    cout << "Digite un numero entero: ";
    cin >> x;
    cout << "Digite otro numero entero: ";
    cin >> y;
    cout << "Digite un caracter (+, -, *, /, %): ";
    cin >> operacion;

    if (operacion == '+')
        cout << x << " + " << y << " = " << x+y;
    else if (operacion == '-')
        cout << x << " - " << y << " = " << x-y;
    else if (operacion == '*')
        cout << x << " * " << y << " = " << x*y;
    else if (operacion == '/') //Devuelve el cociente
        cout << x << " / " << y << " = " << x/y;
    else if (operacion == '%') // devuelve el resto
        cout << x << " % " << y << " = " << x%y;
    else
        cout << "Operador desconocido" << endl;

  return 0;
}

#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
	int numero;

	cout<<"INGRESE UN NUMERO: ";
	cin>>numero;



	for(int i=1; i<=100; i++){
		cout<<numero<<" * "<<i<<" = "<<numero * i<<endl;
	}
	return 0;
}

#include <iostream>

using namespace std;

int main() {
    int num,s=0,i=0;
    bool bandera=true;
    float promedio;

    cout << "Para terminar ingrese un multiplo de 13" << endl;

    while(bandera) {
        cout << "Ingrese un numero:";
        cin >> num;
        if (num % 13 == 0)
            bandera = false;
        else if (num % 2 == 0) {
            s = s + num;
            i++;
        }
    }

    promedio = s / (float)i;
    cout << "El promedio de los numeros es " << promedio << endl;

    return 0;
}

#include <iostream>

int main()
{
    int suma = 0;

    for( int i = 1; i <= 100; i++ ){
        if( i % 2 == 0 ) suma += i;
    }

    std::cout << "\nLa suma de los numeros pares es: " << suma << std::endl;

    return 0;
}

#include <iostream>

using namespace std;

int main() {
    int num,s=0,i=0;
    bool bandera=true;
    float promedio;

    cout << "Para terminar ingrese un multiplo de 13" << endl;

    while(bandera) {
        cout << "Ingrese un numero:";
        cin >> num;
        if (num % 13 == 0)
            bandera = false;
        else if (num % 2 == 0) {
            s = s + num;
            i++;
        }
    }

    promedio = s / (float)i;
    cout << "El promedio de los numeros es " << promedio << endl;

    return 0;
}


#include <iostream>
using namespace std;

int main()
{
    string str;
    
    cout <<"Cadena de texto:"<< endl; 
    cin >> str;
    

    int length = str.size();

    cout<<"Character at last position: "<<str.at(length-1)<<endl;

}