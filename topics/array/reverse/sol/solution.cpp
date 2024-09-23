// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> numbers;
    for (int i = 0; i < 13; i++) {
        int a;
        cin >> a;
        numbers.push_back(a);
    }
    cout << numbers[0];
    for (int i = 1; i < 13; i++) {
        cout << " " << numbers[i];
    }
    cout << "\n" << numbers[12];
    for (int i = 11; i >= 0; i--) {
        cout << " " << numbers[i];
    }
    cout << "\n";
    return 0;
}
