
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }
    vector<int> win(N - 1);
    for (int i = 0; i < N - 1; ++i) {
        win[i] = A[i + 1] - A[i];
    }
    vector<int> diff(N - 2);
    for (int i = 0; i < N - 2; ++i) {
        diff[i] = win[i + 1] - win[i];
    }
    for (int i = 0; i < N - 1; ++i) {
        cout << win[i] << " ";
    }
    cout << "\n";
    for (int i = 0; i < N - 2; ++i) {
        cout << diff[i] << " ";
    }
    cout << "\n";
    return 0;
}
