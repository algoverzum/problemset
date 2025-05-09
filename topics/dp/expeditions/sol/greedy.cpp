#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

struct Permit {
    int start, end, credits;
    int index;
    double credit_per_sector;
};

bool compareByDensity(const Permit &a, const Permit &b) {
    if (a.credit_per_sector != b.credit_per_sector)
        return a.credit_per_sector > b.credit_per_sector;
    return a.index < b.index;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<Permit> permits(n);
    for (int i = 0; i < n; i++) {
        cin >> permits[i].start >> permits[i].end >> permits[i].credits;
        permits[i].index = i + 1;
        int length = permits[i].end - permits[i].start + 1;
        permits[i].credit_per_sector = (double)permits[i].credits / length;
    }

    sort(permits.begin(), permits.end(), compareByDensity);

    vector<bool> occupied(m + 2, false);
    vector<int> selected;
    int totalCredits = 0;

    for (const auto &permit : permits) {
        bool canTake = true;
        for (int sector = permit.start; sector <= permit.end; sector++) {
            if (occupied[sector]) {
                canTake = false;
                break;
            }
        }
        if (canTake) {
            for (int sector = permit.start; sector <= permit.end; sector++) {
                occupied[sector] = true;
            }
            selected.push_back(permit.index);
            totalCredits += permit.credits;
        }
    }
    cout << totalCredits << endl;
    sort(selected.begin(), selected.end());
    // reverse(selected.begin(),selected.end());
    for (int id : selected) {
        cout << id << " ";
    }
    cout << endl;

    return 0;
}