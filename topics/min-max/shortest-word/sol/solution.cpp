// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<string> words(N);
    for (int i = 0; i < N; i++) {
        cin >> words[i];
    }
    string shortest_word = words[0];
    int shortest_length = words[0].size();
    for (int i = 1; i < N; i++) {
        if (words[i].size() < shortest_length) {
            shortest_word = words[i];
            shortest_length = words[i].size();
        }
    }
    cout << shortest_word << '\n';
    return 0;
}