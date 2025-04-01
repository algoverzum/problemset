#include <iostream>
#include <vector>
using namespace std;

// Define a function called odd_numbers here.

// Do not change anything below.
int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }
    vector<int> odds = odd_numbers(numbers);
    for (int odd : odds) {
        cout << odd << " ";
    }
    cout << "\n";
}
