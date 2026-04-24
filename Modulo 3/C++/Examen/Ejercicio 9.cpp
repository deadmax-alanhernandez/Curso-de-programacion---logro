#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> comidas(3);
    for(int it = 0; it < 3; it++) {
        cout << "Comida " << it+1 << ": ";
        cin >> comidas[it];
    }

    for(string c : comidas) { // 
        cout << "Te gustan las siguientes comidas: " << c << endl;
    }
    return 0;
}