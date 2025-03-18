// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int first_even(vector<int> numbers) {
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] % 2 == 0) {
            return i;
        }
    }
    return -1;
}
int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        cin >> numbers[i];
    }

    cout << first_even(numbers) << "\n";
}
