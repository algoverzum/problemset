// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;
int main() {
    int N;
    cin >> N;
    vector<vector<int>> weeks(N, vector<int>(7));
    long long maxSum = -1;
    int maxWeek = -1;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 7; j++) {
            cin >> weeks[i][j];
        }
    }
    // Összegzés + maximális hét keresése
    for (int i = 0; i < N; i++) {
        long long sum = 0;
        for (int j = 0; j < 7; j++) {
            sum += weeks[i][j];
        }
        if (sum >= maxSum) {
            maxSum = sum;
            maxWeek = i + 1; // +1 mert sorszám 1-től indul
        }
    }
    cout << maxWeek << endl;
    return 0;
}