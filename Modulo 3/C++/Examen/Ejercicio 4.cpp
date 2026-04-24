#include <iostream>
#define LIMITE 10
using namespace std;

int main() {
    int num;
    cout << "Introduce un numero: ";
    cin >> num;

    for (int it = 1; it <= LIMITE; it++) {
        cout << num << " x " << it << " = " << num * it << endl;
    }
    return 0;
}