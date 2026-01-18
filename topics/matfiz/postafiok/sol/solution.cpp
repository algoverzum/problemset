// @check-accepted: *
#include <iostream>
#include <string>
using namespace std;

int main() {
    string cim, postafiok = "", postahivatal = "";
    cin >> cim;
    int i = 0;
    while (cim[i] != '@') {
        postafiok = postafiok + cim[i];
        i++;
    }
    cout << postafiok << "\n";
    i++;
    while (i < cim.size()) {
        postahivatal = postahivatal + cim[i];
        i++;
    }
    cout << postahivatal << "\n";
    return 0;
}
