#include <iostream>
#include <string>

using namespace std;

class CajaFuerte {
private: 
    int pinSecreto;
    bool estadoAbierto;

public:
  CajaFuerte (int pinInicial) {
    pinSecreto = pinInicial; 
    estadoAbierto = false;
  }
  bool intentarAbrir(int pinIngresado) {
    if (pinIngresado == pinSecreto){
        estadoAbierto = true;
        return true;
    }
    else {
        estadoAbierto = false;
        return false;
    }
  }
};

int main(){
    CajaFuerte Caja(2408);

    int intento;
    bool exito;

    cout << "Sistema de seguridad de la caja fuerte" << endl;

    do{
        cout << "Ingrese el PIN correcto (4 digitos): ";
        cin >> intento;
        
        exito = Caja.intentarAbrir(intento);

        if (exito == false) {
            cout << "Acceso denegado. Intente de nuevo" << endl;
        }

    } while (exito == false);

    cout << "PIN correcto, tiene acceso a la caja fuerte" << endl;
    
    return 0;
    
}