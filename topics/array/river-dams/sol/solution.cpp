// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> width(n);

    for (int i = 0; i < n; i++) {
        cin >> width[i];
    }

    int count = 0;
    for (int i = 1; i < n - 1; i++) {
        if (width[i - 1] < width[i] && width[i] > width[i + 1]) {
            count++;
        }
    }
    cout << count << "\n";
}
