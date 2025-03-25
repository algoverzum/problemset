// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {

    int N, M;
    cin >> N;
    set<string> fruits1, fruits2;
    string fruit;

    for (int i = 0; i < N; i++) {
        cin >> fruit;
        fruits1.insert(fruit);
    }

    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> fruit;
        fruits2.insert(fruit);
    }

    vector<string> uniqueFruits;
    for (string f : fruits1) {
        if (!fruits2.count(f))
            uniqueFruits.push_back(f);
    }
    for (string f : fruits2) {
        if (!fruits1.count(f))
            uniqueFruits.push_back(f);
    }
    sort(uniqueFruits.begin(), uniqueFruits.end());

    cout << uniqueFruits.size() << '\n';
    for (string f : uniqueFruits) {
        cout << f << '\n';
    }

    return 0;
}
