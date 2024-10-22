// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    int young_adults = 0;
    for (int i = 0; i < n; i++) {
        int age;
        cin >> age;
        if (age >= 18 && age < 21) {
            young_adults++;
        }
    }
    cout << young_adults / 3 << "\n";
}
