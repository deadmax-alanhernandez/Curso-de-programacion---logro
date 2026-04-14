#include <iostream>
#include <vector>

class DispositivoRed {
public:
    std::string ip;
    DispositivoRed(std::string _ip) : ip(_ip) {}
};

class RouterCore : public DispositivoRed {
private:
    int paquetesDescartados = 0;
    int totalProcesados = 0;

public:
    RouterCore(std::string _ip) : DispositivoRed(_ip) {}

    void rutearPaquete(int puerto) {
        totalProcesados++;
        switch (puerto) {
            case 80: std::cout << "Ruteando tráfico HTTP...\n"; break;
            case 21: std::cout << "Ruteando tráfico FTP...\n"; break;
            case 25: std::cout << "Ruteando tráfico SMTP...\n"; break;
            default: 
                paquetesDescartados++;
                std::cout << "Puerto no soportado. Paquete descartado.\n";
        }
    }

    std::string verificarCongestion() {
    
        if (totalProcesados > 0 && (float)paquetesDescartados / totalProcesados > 0.10) {
            return "Congestión Severa";
        } else {
            return "Red Estable";
        }
    }

    void procesarFlujo() {
        while (verificarCongestion() == "Red Estable") {
            int puerto;
            std::cout << "Puerto de entrada (80, 21, 25) o 0 para salir: ";
            std::cin >> puerto;
            if (puerto == 0) break;
            rutearPaquete(puerto);
            std::cout << "Estado: " << verificarCongestion() << "\n";
        }
        if (verificarCongestion() == "Congestión Severa") {
            std::cout << "Protocolo de emergencia activado por congestión.\n";
        }
    }
};