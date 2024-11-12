// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> candies;
    int a;
    for (int i = 0; i < n; i++) {
        cin >> a;
        candies.push_back(a);
    }
    int maxc = 0;
    int maxid = 0;
    int minc = 10000;
    int minid = 0;
    for (int i = 0; i < n; i++) {
        if (candies[i] > maxc) {
            maxc = candies[i];
            maxid = i;
        }
        if (candies[i] < minc) {
            minc = candies[i];
            minid = i;
        }
    }
    candies[minid] = maxc;
    candies[maxid] = minc;
    for (int i = 0; i < n; i++) {
        cout << candies[i] << " ";
    }
    cout << "\n";
}
