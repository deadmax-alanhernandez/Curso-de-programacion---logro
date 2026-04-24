#include <iostream>
#include <string>

class EstacionMonitoreo {
protected:
    std::string ubicacion;
public:
    EstacionMonitoreo(std::string loc) : ubicacion(loc) {}
};

class NodoCentralSismico : public EstacionMonitoreo {
private:
    double energiaAcumulada = 0.0;
    const double UMBRAL_CRITICO = 500.0;

public:
    NodoCentralSismico(std::string loc) : EstacionMonitoreo(loc) {}

    void clasificarOnda(int tipo) {
        switch (tipo) {
            case 1: energiaAcumulada += 10.5; std::cout << "Onda P detectada.\n"; break;
            case 2: energiaAcumulada += 25.0; std::cout << "Onda S detectada.\n"; break;
            case 3: energiaAcumulada += 100.2; std::cout << "Onda Superficial (Peligro) detectada.\n"; break;
            default: std::cout << "Ruido sísmico insignificante.\n";
        }
    }

    bool evaluarRiesgo() {
        if (energiaAcumulada > UMBRAL_CRITICO) {
            return true; 
        } else {
            return false;
        }
    }

    void iniciarSistema() {
        
        for (int i = 1; i <= 5; i++) {
            std::cout << "Calibrando sensor " << i << "...\n";
        }

        
        while (!evaluarRiesgo()) {
            int lectura;
            std::cout << "Energía actual: " << energiaAcumulada << ". Ingrese tipo de onda (1-3) o 0 para esperar: ";
            std::cin >> lectura;
            if (lectura == 0) break;
            clasificarOnda(lectura);
        }
        
        if (evaluarRiesgo()) std::cout << "¡ALERTA! Riesgo estructural detectado en " << ubicacion << "\n";
    }
};

int main() {
    NodoCentralSismico nodo("CDMX - Zona Centro");
    nodo.iniciarSistema();
    return 0;
}