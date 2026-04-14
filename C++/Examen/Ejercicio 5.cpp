#include <iostream>
using namespace std;

int main() {
    int numeroSecreto = 68;
    int intento = 0;

    while (intento != numeroSecreto) {
        cout << "Adivina el numero: ";
        cin >> intento;

        if (intento < numeroSecreto) cout << "Mas alto..." << endl;
        else if (intento > numeroSecreto) cout << "Mas bajo..." << endl;
    }

    cout << "¡Felicidades!, Adivinaste." << endl;
    return 0;
}