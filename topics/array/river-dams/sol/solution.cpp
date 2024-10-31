// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> sections(n);

    for (int i = 0; i < n; i++) {
        cin >> sections[i];
    }

    int count = 0;
    for (int i = 1; i < n - 1; i++) {
        if (sections[i - 1] < sections[i] && sections[i] > sections[i + 1]) {
            count++;
        }
    }
    cout << count << "\n";
}
