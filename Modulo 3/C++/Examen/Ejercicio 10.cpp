#include <iostream>
using namespace std;

const double PI = 3.14159;

void calcularPerimetro(double radio) {
    double perimetro = 2 * PI * radio;
    cout << "El perimetro es: " << perimetro << endl;
}

int main() {
    double r;
    cout << "Radio del circulo: ";
    cin >> r;
    calcularPerimetro(r);
    return 0;
}