// @check-accepted: *
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<string> received;
    for (int i = 0; i < N; i++) {
        string source;
        int frequency;
        cin >> source;
        cin >> frequency;
        if (frequency >= 500) {
            received.push_back(source);
        }
    }

    cout << received.size();
    for (string source : received) {
        cout << " " << source;
    }
    cout << "\n";

    return 0;
}