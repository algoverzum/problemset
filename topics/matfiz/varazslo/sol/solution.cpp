// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    string s;
    cin >> s;

    vector<char> numbers;

    for (size_t i = 0; i < s.size(); i += 2) {
        numbers.push_back(s[i]);
    }

    sort(numbers.begin(), numbers.end());

    for (size_t i = 0; i < numbers.size(); ++i) {
        if (i > 0)
            cout << '+';
        cout << numbers[i];
    }
    cout << '\n';

    return 0;
}
