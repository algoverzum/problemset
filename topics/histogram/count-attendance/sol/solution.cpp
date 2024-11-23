// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> attendances(n);
    for (int i = 0; i < n; i++) {
        cin >> attendances[i];
    }
    vector<int> histogram(11, 0);
    for (int attendance : attendances) {
        histogram[attendance] += 1;
    }
    for (int i = 0; i <= 10; i++) {
        cout << histogram[i] << " ";
    }
    cout << '\n';
}
