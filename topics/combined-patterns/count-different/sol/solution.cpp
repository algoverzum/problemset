// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }
    vector<int> unique_numbers;
    for (int i = 0; i < n; i++) {
        auto it =
            find(unique_numbers.begin(), unique_numbers.end(), numbers[i]);
        if (it == unique_numbers.end()) {
            unique_numbers.push_back(numbers[i]);
        }
    }
    cout << unique_numbers.size() << "\n";
}
