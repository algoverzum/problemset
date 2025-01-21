// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arrivals(1000001, 0);
    vector<int> leaves(1000001, 0);
    for (int i = 0; i < n; i++) {
        int arr, leave;
        cin >> arr >> leave;
        arrivals[arr] += 1;
        leaves[leave] += 1;
    }
    int result = 0;
    int current = 0;
    for (int i = 0; i < 1000001; i++) {
        current += arrivals[i];
        if (result < current)
            result = current;
        current -= leaves[i];
    }
    cout << result << "\n";
}
