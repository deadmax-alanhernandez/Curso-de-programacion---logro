#include <iostream>
#include <string>

class MaquinariaPesada {
public:
    int idMaquina;
    MaquinariaPesada(int id) : idMaquina(id) {}
};

class IncineradorInteligente : public MaquinariaPesada {
private:
    float temperaturaHorno = 25.0f; 
public:
    IncineradorInteligente(int id) : MaquinariaPesada(id) {}

    
    void precalentar() {
        std::cout << "[INICIO] Iniciando precalentamiento del incinerador " << idMaquina << "...\n";
        while (temperaturaHorno < 800.0f) {
            temperaturaHorno += 150.5f;
            std::cout << "Calentando... Temp actual: " << temperaturaHorno << "°C\n";
        }
        std::cout << "[OK] Temperatura de operación alcanzada.\n";
    }

   
    std::string procesarMaterial(int material) {
        float tempNecesaria = 0.0f;
        
        switch (material) {
            case 1: tempNecesaria = 500.0f; break;  
            case 2: tempNecesaria = 1200.0f; break; 
            case 3: tempNecesaria = 300.0f; break;  
            default: return "Error: Material no identificado.";
        }

        
        if (temperaturaHorno >= tempNecesaria) {
            return "Éxito: Residuo incinerado al 100%.";
        } else {
            return "Fallo: Temperatura insuficiente para este material.";
        }
    }

    void operarCinta() {
        int estadoCinta;
        precalentar();

        do {
            int tipoMaterial;
            std::cout << "\n--- Cinta en movimiento ---" << std::endl;
            std::cout << "Ingrese material (1:Plástico, 2:Metal, 3:Orgánico): ";
            std::cin >> tipoMaterial;

            std::cout << procesarMaterial(tipoMaterial) << std::endl;

            std::cout << "¿Continuar turno? (1: Sí / 0: Fin del turno): ";
            std::cin >> estadoCinta;
        } while (estadoCinta != 0);

        std::cout << "Cinta transportadora detenida. Fin de jornada.\n";
    }
};

int main() {
    IncineradorInteligente incinerador(9001);
    incinerador.operarCinta();
    return 0;
}