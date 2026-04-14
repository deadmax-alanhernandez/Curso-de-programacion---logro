
#include <iostream>
#include <cmath>
#include <string>

#define PI 3.14159265

using namespace std;

void mostrarMenu() {
    cout << "SUMA" << endl;
    cout << "RESTA" << endl;
    cout << "MULTIPLICACION" << endl;
    cout << "DIVISION" << endl;
    cout << "POTENCIA" << endl;
    cout << "RAIZ" << endl;
    cout << "SENO" << endl;
    cout << "COSENO" << endl;
    cout << "TANGENTE" << endl;
    cout << "LOGARITMO" << endl;
    cout << "FACTORIAL" << endl;
    cout << "SALIR" << endl;
    cout << "Seleccione su operacion: ";
}

double sumar(double a, double b) { return a + b; }
double restar(double a, double b) { return a - b; }
double multiplicar(double a, double b) { return a * b; }
double dividir(double a, double b) { return a / b; }
double potenciar(double a, double b) { return pow(a, b); }

long long calcularFactorial(int n) {
    long long res = 1;
    for (int i = 1; i <= n; i++) {
        res *= i;
    }
    return res;
}

int main() {
    double num1;
    double num2;
    double resultado;
    string opcion;

    do {
        mostrarMenu();
        cin >> opcion;

        if (opcion == "SUMA") {
            cout << "Introduce el primer numero: "; cin >> num1;
            cout << "Introduce el segundo numero: "; cin >> num2;
            resultado = sumar(num1, num2);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "RESTA") {
            cout << "Introduce el primer numero: "; cin >> num1;
            cout << "Introduce el segundo numero: "; cin >> num2;
            resultado = restar(num1, num2);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "MULTIPLICACION") {
            cout << "Introduce el primer numero: "; cin >> num1;
            cout << "Introduce el segundo numero: "; cin >> num2;
            resultado = multiplicar(num1, num2);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "DIVISION") {
            cout << "Introduce el dividendo: "; cin >> num1;
            cout << "Introduce el divisor: "; cin >> num2;
            while (num2 == 0) {
                cout << "Numero No Admitido. Introduce un divisor distinto de cero: ";
                cin >> num2;
            }
            resultado = dividir(num1, num2);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "POTENCIA") {
            cout << "Introduce la base: "; cin >> num1;
            cout << "Introduce el exponente: "; cin >> num2;
            resultado = potenciar(num1, num2);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "RAIZ") {
            cout << "Introduce el numero: "; cin >> num1;
            while (num1 < 0) {
                cout << "Numero No Admitido. Introduce un numero no negativo: ";
                cin >> num1;
            }
            resultado = sqrt(num1);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "SENO") {
            cout << "Introduce el numero: "; cin >> num1;
            resultado = sin(num1 * PI / 180);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "COSENO") {
            cout << "Introduce el numero: "; cin >> num1;
            resultado = cos(num1 * PI / 180);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "TANGENTE") {
            cout << "Introduce el numero: "; cin >> num1;
            resultado = tan(num1 * PI / 180);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "LOGARITMO") {
            cout << "Introduce el numero: "; cin >> num1;
            while (num1 <= 0) {
                cout << "Numero No Admitido. Introduce un numero mayor a cero: ";
                cin >> num1;
            }
            resultado = log(num1);
            cout << "Resultado: " << resultado << endl;
        } 
        else if (opcion == "FACTORIAL") {
            int n;
            cout << "Introduce el numero: "; cin >> n;
            while (n < 0) {
                cout << "Numero No Admitido. Introduce un entero positivo: ";
                cin >> n;
            }
            cout << "Resultado: " << calcularFactorial(n) << endl;
        } 
        else if (opcion != "SALIR") {
            cout << "Opcion no valida." << endl;
        }

    } while (opcion != "SALIR");

    return 0;
}