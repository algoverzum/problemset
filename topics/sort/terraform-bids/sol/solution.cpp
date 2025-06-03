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
        string company;
        int bid;
        cin >> company >> bid;
        offers.emplace_back(bid, company);
    }

    sort(offers.begin(), offers.end());

    for (auto [bid, company] : offers) {
        cout << company << '\n';
    }

    return 0;
}