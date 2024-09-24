// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> numbers(13);
    for (int i = 0; i < 13; i++) {
        cin >> numbers[i];
    }
    for (int i = 0; i < 13; i++) {
        cout << numbers[i] << " ";
    }
    cout << "\n";
    for (int i = 12; i >= 0; i--) {
        cout << numbers[i] << " ";
    }
    cout << "\n";
    return 0;
}
