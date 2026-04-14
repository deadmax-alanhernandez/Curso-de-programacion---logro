#include <iostream>
using namespace std;

int main() {
    int opcion;
    do {
        cout << "\n1. Saludar";
        cout << "\n2. Despedirse";
        cout << "\n3. Salir";
        cin >> opcion;

        switch(opcion) {
            case 1: cout << "\nHola" << endl; break;
            case 2: cout << "\nAdiós" << endl; break;
            case 3: cout << "\nSaliendo..." << endl; break;
            default: cout << "\nOpcion invalida." << endl;
        }
    } while (opcion != 3);
    return 0;
}