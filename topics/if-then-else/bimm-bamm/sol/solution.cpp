// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    if (n % 15 == 0) {
        cout << "bumm" << "\n";
    } else if (n % 5 == 0) {
        cout << "bamm" << "\n";
    } else if (n % 3 == 0) {
        cout << "bimm" << "\n";
    } else {
        cout << n << "\n";
    }
    return 0;
}
