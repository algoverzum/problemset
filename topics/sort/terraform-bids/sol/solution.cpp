// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int offerCount;
    cin >> offerCount;

    vector<pair<int, string>> offers;

    for (int i = 0; i < offerCount; i++) {
        string companyName;
        int cost;
        cin >> companyName >> cost;
        offers.emplace_back(cost, companyName);
    }

    sort(offers.begin(), offers.end());

    for (const auto &offer : offers) {
        cout << offer.second << '\n';
    }

    return 0;
}