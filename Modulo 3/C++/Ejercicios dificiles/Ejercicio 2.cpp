#include <iostream>

class InstalacionIndustrial {
public:
    std::string idPlanta;
    InstalacionIndustrial(std::string id) : idPlanta(id) {}
};

class ReactorQuimico : public InstalacionIndustrial {
private:
    float presionInterna = 0.0f;

public:
    ReactorQuimico(std::string id) : InstalacionIndustrial(id) {}

    float obtenerMaxPresion(int fase) {
        switch (fase) {
            case 1: return 150.0f; // Calentamiento
            case 2: return 300.0f; // Fusión
            case 3: return 100.0f; // Enfriamiento
            default: return 50.0f;
        }
    }

    void inyectarReactivo(float cantidad, int faseActual) {
        float limite = obtenerMaxPresion(faseActual);
        if (presionInterna + cantidad <= limite) {
            presionInterna += cantidad;
            std::cout << "Inyección exitosa. Presión: " << presionInterna << " PSI.\n";
        } else {
            std::cout << "CRÍTICO: Inyección rechazada por sobrepresión.\n";
        }
    }

    void operar() {
        int codigo;
        do {
            int fase;
            float inyeccion;
            std::cout << "\nFase (1:Cal, 2:Fus, 3:Enf): "; std::cin >> fase;
            std::cout << "Cantidad a inyectar: "; std::cin >> inyeccion;
            
            inyectarReactivo(inyeccion, fase);

            std::cout << "Ingrese 999 para apagado de emergencia, otro para continuar: ";
            std::cin >> codigo;
        } while (codigo != 999);
        std::cout << "Sistema de reactor " << idPlanta << " apagado.\n";
    }
};

int main() {
    ReactorQuimico reactor("RX-204");
    reactor.operar();
    return 0;
}