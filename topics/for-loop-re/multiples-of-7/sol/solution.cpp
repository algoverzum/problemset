// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    for (int i = a + 1; i < b; i++) {
        if (i % 7 == 0) {
            cout << i << " ";
        }
    }
    cout << "\n";
}
