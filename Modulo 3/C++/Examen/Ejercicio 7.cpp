#include <iostream>
using namespace std;

float Prototipo(float b, float h); 

int main() {
    float base, altura;
    cout << "Base: "; cin >> base;
    cout << "Altura: "; cin >> altura;
    cout << "Area: " << Prototipo(base, altura) << endl;
    return 0;
}

float Prototipo(float b, float h) {
    return b * h;
}