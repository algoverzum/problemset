#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N;
    vector<string> fruits1;

    for (int i = 0; i < N; ++i) {
        string fruit;
        cin >> fruit;
        fruits1.push_back(fruit);
    }

    cin >> M;
    vector<string> fruits2;

    for (int i = 0; i < M; ++i) {
        string fruit;
        cin >> fruit;
        fruits2.push_back(fruit);
    }

    vector<string> exclusive;
    for (const string &f1 : fruits1) {
        bool found = false;
        for (const string &f2 : fruits2) {
            if (f1 == f2) {
                found = true;
                break;
            }
        }
        if (!found)
            exclusive.push_back(f1);
    }

    for (const string &f2 : fruits2) {
        bool found = false;
        for (const string &f1 : fruits1) {
            if (f1 == f2) {
                found = true;
                break;
            }
        }
        if (!found)
            exclusive.push_back(f2);
    }
    sort(exclusive.begin(), exclusive.end());
    cout << exclusive.size() << "\n";
    for (const string &fruit : exclusive) {
        cout << fruit << "\n";
    }

    return 0;
}