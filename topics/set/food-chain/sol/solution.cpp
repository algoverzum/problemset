// @check-accepted: *
#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;

    set<string> animals;
    set<string> predators;
    string eater, food;
    vector<pair<string, string>> pairs(N);

    for (int i = 0; i < N; i++) {
        cin >> eater >> food;
        animals.insert(eater);
        pairs[i] = {eater, food};
    }

    for (int i = 0; i < N; i++) {
        if (animals.count(pairs[i].second)) {
            predators.insert(pairs[i].first);
        }
    }

    cout << predators.size() << "\n";
    for (const string &name : predators) {
        cout << name << "\n";
    }

    return 0;
}
