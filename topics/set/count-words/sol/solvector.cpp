// @check-accepted: examples
// @check-time-limit-exceeded: all
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> words;
    for (int i = 0; i < n; i++) {
        string curword;
        cin >> curword;
        if (find(words.begin(), words.end(), curword) == words.end()) {
            words.push_back(curword);
        }
    }
    cout << words.size() << "\n";
}
