// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> deadlines(n + 2);
    for (int i = 0; i < n; i++) {
        cin >> deadlines[i];
    }

    vector<int> result;
    int day = 1;
    for (int i = 0; i < n; i++) {
        if (day <= deadlines[i]) {
            if (deadlines[i + 1] == deadlines[i]) {
                result.push_back(i + 2);
                day++;
            } else {
                result.push_back(i + 1);
                day++;
            }
        }
    }

    cout << result.size() << "\n";
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << "\n";

    return 0;
}
