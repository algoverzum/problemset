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

        if (count(numbers.begin(), numbers.end(), numbers[i]) == 1) {
            unique_numbers.push_back(numbers[i]);
        }
    }
    if (unique_numbers.size() == 0) {
        cout << -1;
    } else {
        cout << *min_element(unique_numbers.begin(), unique_numbers.end());
    }
}
