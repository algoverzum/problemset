// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<string> english_words(n);
    vector<string> alien_words(n);
    for (int i = 0; i < n; ++i) {
        cin >> english_words[i] >> alien_words[i];
    }

    int m;
    cin >> m;
    vector<string> message(m);
    for (int i = 0; i < m; ++i) {
        cin >> message[i];
    }

    for (const string &word : message) {
        for (int i = 0; i < english_words.size(); i++) {
            if (word == english_words[i]) {
                cout << alien_words[i] << "\n";
                break;
            }
        }
    }

    return 0;
}