// @check-accepted: *
#include <iostream>
#include <map>
using namespace std;

int main() {
    int n;
    cin >> n;
    map<string, int> votecount;
    for (int i = 0; i < n; i++) {
        string name;
        int votes;
        cin >> name >> votes;
        votecount[name] += votes;
    }
    for (auto candidate : votecount) {
        cout << candidate.first << " " << candidate.second << "\n";
    }
}
