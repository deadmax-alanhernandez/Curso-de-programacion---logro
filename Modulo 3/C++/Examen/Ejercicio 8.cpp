#include <iostream>
using namespace std;

void modificarPorValor(int n) { n += 10; }
void modificarPorReferencia(int &n) { n += 10; }

int main() {
    int numero = 20;
    
    modificarPorValor(numero);
    cout << "Tras valor: " << numero << endl; 

    modificarPorReferencia(numero);
    cout << "Tras referencia: " << numero << endl;
    return 0;
}