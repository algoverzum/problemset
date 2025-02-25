// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> heights(N);
    for (int i = 0; i < N; i++) {
        cin >> heights[i];
    }
    int maxLength = 1, endIndex = -1, currentLength = 1;
    for (int i = 1; i < N; i++) {
        if (heights[i] > heights[i - 1]) {
            currentLength++;
        } else {
            if (currentLength > maxLength) {
                maxLength = currentLength;
                endIndex = i;
            }
            currentLength = 1;
        }
    }
    if (currentLength > maxLength) {
        maxLength = currentLength;
        endIndex = N;
    }
    if (maxLength > 1) {
        cout << endIndex - maxLength + 1 << " " << endIndex << "\n";
    } else {
        cout << -1 << "\n";
    }
    return 0;
}