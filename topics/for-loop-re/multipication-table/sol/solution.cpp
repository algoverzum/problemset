// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cout << i;
        for (int j = 2; j <= n; j++) {
            cout << " " << i * j;
        }
        cout << "\n";
    }
}
