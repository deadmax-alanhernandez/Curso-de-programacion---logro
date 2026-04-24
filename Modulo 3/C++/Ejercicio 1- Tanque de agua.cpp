#include <iostream>

class Tanqueagua {
private:
    double capacidadmax;
    double nivelactual;

public:
    Tanqueagua(float capacidad) : capacidadmax(capacidad), nivelactual(0.0) {
        if (capacidad <= 0) {
            
        }
    }

    double getNivelActual() const {
        return nivelactual;
    }

    double getcapacidadmax() const {
        return capacidadmax;
    }

    void llenarTanque(double flujo) {
        
        if (flujo <= 0) return; 

        nivelactual += flujo;

        if (nivelactual > capacidadmax) {
            nivelactual = capacidadmax; 
        }
    }
};

int main() {
    Tanqueagua tanque(500.0);
    double flujo = 50;

    std::cout << "Capacidad: 500L\n";

while (tanque.getNivelActual() < tanque.getcapacidadmax()) {
    tanque.llenarTanque(flujo);
    std::cout << "Nivel actual: " << tanque.getNivelActual() << "L\n";
}
    std::cout << "Tanque lleno.\n";
    return 0;
}