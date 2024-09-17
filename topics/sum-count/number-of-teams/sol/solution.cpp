// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int young_adults = 0;
    int a_i;
    for (int i = 0; i < n; i++) {
        cin >> a_i;
        if (a_i >= 18 && a_i < 21) {
            young_adults++;
        }
    }
    cout << young_adults / 3 << "\n";
}
