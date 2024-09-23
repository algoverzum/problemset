// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    int counter = 0;
    vector<int> numerals;
    for (int i = 0; i < n; i++) {
        int current;
        cin >> current;
        if (current <= 4) {
            counter++;
            numerals.push_back(i + 1);
        }
    }
    cout << counter << "\n";
    for (int i = 0; i < counter; i++) {
        cout << numerals[i] << " ";
    }
    cout << "\n";
    return 0;
}
