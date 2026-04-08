#include <iostream>
#include <cmath>
#define PI 3.14159265

int main(){

    double num1;
    double num2;
    double resultado;
    
    int opcion; 

    std::cout << "SUMA - 1" << std::endl;
    std::cout << "RESTA - 2" << std::endl;
    std::cout << "MULTIPLICACION - 3" << std::endl;
    std::cout << "DIVISION - 4" << std::endl;
    std::cout << "POTENCIA - 5" << std::endl;
    std::cout << "RAIZ CUADRADA - 6" << std::endl;
    std::cout << "SENO - 7" << std::endl;
    std::cout << "COSENO - 8" << std::endl;
    std::cout << "TANGENTE - 9" << std::endl;
    std::cout << "LOGARITMO NEPERIANO - 10" << std::endl;
    std::cout << "Seleccione su operacion: " << std::endl;
    std::cin >> opcion;

    
    switch (opcion){


    case 1:
        std::cout << "Introduce el primer numero: ";
        std::cin >> num1;
        std::cout << "Introduce el segundo numero: ";
        std::cin >> num2;

        resultado = num1 + num2;
        
        std::cout << "Resultado: " << resultado << std::endl;
        break;
    case 2:
        std::cout << "Introduce el primer numero: ";
        std::cin >> num1;
        std::cout << "Introduce el segundo numero: ";
        std::cin >> num2;

        resultado = num1 - num2;
        
        std::cout << "Resultado: " << resultado << std::endl;
        break;
    case 3:
        std::cout << "Introduce el primer numero: ";
        std::cin >> num1;
        std::cout << "Introduce el segundo numero: ";
        std::cin >> num2;

        resultado = num1 * num2;
        
        std::cout << "Resultado: " << resultado << std::endl;
        break;
    case 4:
        std::cout << "Introduce el primer numero: ";
        std::cin >> num1;
        std::cout << "Introduce el segundo numero: ";
        std::cin >> num2;

        resultado = num1 / num2;
        
        if (num1 && num2 > 0){

           std::cout << "Resultado: " << resultado << std::endl;
            break;
        }
        else {std:: cout << "Numero No Admitido"<< std::endl;
            break;}

        

    case 5:
            
        std::cout << "Introduce el primer numero: ";
        std::cin >> num1;
        std::cout << "Introduce el segundo numero: ";
        std::cin >> num2;

        resultado = pow(num1, num2);
        
        std::cout << "Resultado: " << resultado << std::endl;
        break;
    case 6:
        std::cout << "Introduce el numero: ";
        std::cin >> num1;

        resultado = sqrt(num1);
         
        if (num1 >= 0){

           std::cout << "Resultado: " << resultado << std::endl;
            break;
        }
        else {std:: cout << "Numero No Admitido"<< std::endl;
            break;}

    case 7:
        std::cout << "Introduce el numero: ";
        std::cin >> num1;

        resultado = sin (num1*PI/180);
        
        std::cout << "Resultado: " << resultado << std::endl;
        break;
    case 8:
        std::cout << "Introduce el numero: ";
        std::cin >> num1;

        resultado = cos (num1*PI/180);
        
        std::cout << "Resultado: " << resultado << std::endl;
        break;
    case 9:
        std::cout << "Introduce el numero: ";
        std::cin >> num1;

        resultado = tan (num1*PI/180);
        
        std::cout << "Resultado: " << resultado << std::endl;
        break;
    case 10:
        std::cout << "Introduce el numero: ";
        std::cin >> num1;

        resultado = log (num1);
        
        std::cout << "Resultado: " << resultado << std::endl;
        break;
    default:
        std::cout << "Nada";
        break;
        
    }}


//REALIZADO POR: Alan Hernandez - Adrian Vera - Jose Franco - Javier Medina - Carlos