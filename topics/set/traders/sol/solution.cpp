// @check-accepted: *
#include <iostream>
#include <unordered_set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N;
    unordered_set<string> fruits1, fruits2, uniqueFruits;
    string fruit;

    for (int i = 0; i < N; i++) {
        cin >> fruit;
        fruits1.insert(fruit);
        uniqueFruits.insert(fruit);
    }

    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> fruit;
        fruits2.insert(fruit);
        if (uniqueFruits.count(fruit))
            uniqueFruits.erase(fruit);
        else
            uniqueFruits.insert(fruit);
    }

    cout << uniqueFruits.size() << '\n';
    for (const string &f : uniqueFruits) {
        cout << f << '\n';
    }

    return 0;
}
