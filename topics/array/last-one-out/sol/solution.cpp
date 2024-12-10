// @check-accepted: *
#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> numbers(n);
    for (int i = 0; i < n; i++) {
        numbers[i] = i + 1;
    }
    int counting = 0;
    while (numbers.size() > 1) {
        counting += m;
        counting %= numbers.size();
        cout << numbers[counting] << " ";
        numbers.erase(numbers.begin() + counting - 1);
    }
    cout << "\n";
    cout << numbers[0] << "\n";
}
