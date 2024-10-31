
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
    vector<int> day_diff(N - 1);
    for (int i = 0; i < N - 1; ++i) {
        day_diff[i] = A[i + 1] - A[i];
    }
    vector<int> diff_diff(N - 2);
    for (int i = 0; i < N - 2; ++i) {
        diff_diff[i] = day_diff[i + 1] - day_diff[i];
    }
    cout << day_diff[0];
    for (int i = 1; i < N - 1; ++i) {
        cout << " " << day_diff[i];
    }
    cout << "\n" << diff_diff[0];
    for (int i = 1; i < N - 2; ++i) {
        cout << " " << diff_diff[i];
    }
    cout << "\n";
    return 0;
}
