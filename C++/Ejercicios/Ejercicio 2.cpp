#include <iostream>
#include <cmath>

using namespace std;

int main() {
    double num1;
    double num2;
    double resultado;


    cout << "Introduce el primer numero: ";
    cin >> num1;
    cout << "Introduce el segundo numero: ";
    cin >> num2;
    
    resultado = num1 + num2;
    cout << "Resultado Suma: " << resultado << endl;

    resultado = num1 - num2;
    cout << "Resultado Resta: " << resultado << endl;

    resultado = num1 * num2;
    cout << "Resultado Multiplicacion: " << resultado << endl;
    resultado = num1 / num2;
    cout << "Resultado Division: " << resultado << endl;

    resultado = pow(num1, num2);
    cout << "Resultado Potencia: " << resultado << endl;
    resultado = sqrt(num1);
    cout << "Resultado Raiz del primer numero: " << resultado << endl;
  
    return 0;
}
