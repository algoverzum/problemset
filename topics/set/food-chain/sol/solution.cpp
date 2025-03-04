// @check-accepted: *
#include <iostream>
#include <set> //std::set is a sorted container.
using namespace std;

int main() {
    int N;
    cin >> N;

    set<string> animals;
    set<string> carnivores;
    string predator, prey;
    pair<string, string> pairs[30];

    for (int i = 0; i < N; i++) {
        cin >> predator >> prey;
        animals.insert(predator);
        pairs[i] = {predator, prey};
    }

    for (int i = 0; i < N; i++) {
        if (animals.count(pairs[i].second)) {
            carnivores.insert(pairs[i].first);
        }
    }

    cout << carnivores.size() << "\n";
    for (const string &name : carnivores) {
        cout << name << "\n";
    }

    return 0;
}
