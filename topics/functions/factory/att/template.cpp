#include <iostream>
#include <vector>
using namespace std;

int first_even(vector<int> numbers) {
    // Write your code here
}

// Do not change anything below.
int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }
    cout << first_even(numbers) << "\n";
}
