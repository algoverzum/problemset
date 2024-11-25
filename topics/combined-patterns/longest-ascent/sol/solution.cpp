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
    int maxLength = 0, startIndex = -1, endIndex = -1, currentLength = 1,
        currentStart = 0;
    for (int i = 1; i < N; i++) {
        if (heights[i] > heights[i - 1]) {
            currentLength++;
        } else {
            if (currentLength > maxLength) {
                maxLength = currentLength;
                startIndex = currentStart;
                endIndex = i - 1;
            }
            currentLength = 1;
            currentStart = i;
        }
    }
    if (currentLength > maxLength) {
        maxLength = currentLength;
        startIndex = currentStart;
        endIndex = N - 1;
    }
    if (maxLength > 1) {
        cout << startIndex + 1 << " " << endIndex + 1 << "\n";
    } else {
        cout << -1 << "\n";
    }
    return 0;
}