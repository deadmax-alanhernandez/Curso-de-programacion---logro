#include <iostream>
#include <string>

class NaveExploracion {
public:
    std::string nombreMision;
    NaveExploracion(std::string n) : nombreMision(n) {}
};

class SondaAutonoma : public NaveExploracion {
private:
    float desviacionTrayectoria = 0.0f; 
public:
    SondaAutonoma(std::string n) : NaveExploracion(n) {}

    void activarPropulsores() {
        if (desviacionTrayectoria > 0.5f) {
            std::cout << "[SISTEMA] Desviación positiva: Activando propulsor IZQUIERDO.\n";
            desviacionTrayectoria -= 0.2f;
        } else if (desviacionTrayectoria < -0.5f) {
            std::cout << "[SISTEMA] Desviación negativa: Activando propulsor DERECHO.\n";
            desviacionTrayectoria += 0.2f;
        } else {
            std::cout << "[SISTEMA] Trayectoria estable. Propulsores en reposo.\n";
        }
    }

   
    float calcularCorreccion(int tipoObjeto) {
        switch (tipoObjeto) {
            case 1: return 0.85f;  
            case 2: return 0.15f;  
            case 3: return 5.50f;  
            default: return 0.0f;
        }
    }

    void iniciarMision() {
        std::cout << "--- Iniciando Sonda: " << nombreMision << " ---\n";
        
        
        for (int ciclo = 1; ciclo <= 15; ++ciclo) {
            int objetoDetectado;
            std::cout << "\nCiclo #" << ciclo << " - Escaneando entorno...\n";
            std::cout << "Objeto (1: Planeta, 2: Asteroide, 3: Agujero Negro, 0: Vacío): ";
            std::cin >> objetoDetectado;

            
            desviacionTrayectoria += calcularCorreccion(objetoDetectado);
            std::cout << "Desviación actual: " << desviacionTrayectoria << " km.\n";

            activarPropulsores();
        }
        std::cout << "\n--- Ciclo de escaneo completado. Sonda entrando en hibernación. ---\n";
    }
};

int main() {
    SondaAutonoma sonda("Voyager III");
    sonda.iniciarMision();
    return 0;
}