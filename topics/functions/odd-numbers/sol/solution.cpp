// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

vector<int> odd_numbers(vector<int> numbers) {
    vector<int> odds;
    for (int num : numbers) {
        if (num % 2 == 1) {
            odds.push_back(num);
        }
    }
    return odds;
}

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
