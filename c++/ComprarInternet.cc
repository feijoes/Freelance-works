#include <iostream>
#include <string.h> 
#include <string>
#include <cstdlib>
#include <cctype>
using namespace std;
bool checkInteger(char input[])
{  bool isNeg=false; int itr=0;if(strlen(input)==0){return false;} if(input[0]=='-'){isNeg=true;itr=1;} for(int i=itr;i<strlen(input);i++){if(!isdigit(input[i])){return false};}return true;}

int validateInputInt(string tipo_input)
{   while (true){char input[100];cout << "Escriba " << tipo_input << ": " ; cin >> input; if((checkInteger(input))){return  stoi(input);}; cout << "Pusiste alguna informacion invalida, intenta nuevamente\n";}}
string validateInputString(string tipo_input)
{   while (true){char input[100];cout << "Escriba " << tipo_input << ": " ; cin >> input;if(!(checkInteger(input))){return  input;}; cout << "Pusiste alguna informacion invalida, intenta nuevamente\n";}
}
int main()
{   int Mbps;string nombrePersona;int telefonoPersona;int edadPersona;string medios[] = {"pago","Paypal" ,"Credito" ,"Debito"};
        while (true){ cout << "Llene los datos para poder realizar la compra \n";nombrePersona = validateInputString("Nombre de la Persona");edadPersona = validateInputInt("la edad");telefonoPersona = validateInputInt("el numero de telefone (solo numeros)");char Repetir_datos[100];
                      cout << "Deseas escribir devuelta los datos? (si/no): "; cin >> Repetir_datos; if (strcmp(Repetir_datos,"si") == 0){continue;}else{break;}};
    cout<<"Porfavor escribi la cantidad de Mbps que deseas comprar: ";cin >> Mbps;cout << "Escriba tu medio de Pago: ";
    for (int i=1;i <size(medios); i++){cout << i << " " << medios[i]<< endl;} cout << "Compra finalizada\n "<< Mbps <<" Comprados, " "Codigo de compra: " << 14920 + rand();return 0;}