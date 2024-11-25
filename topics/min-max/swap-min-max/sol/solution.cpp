// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> candies(n);
    for (int i = 0; i < n; i++) {
        cin >> candies[i];
    }
    int maxindex = 0, minindex = 0;
    for (int i = 0; i < n; i++) {
        if (candies[i] > candies[maxindex]) {
            maxindex = i;
        }
        if (candies[i] < candies[minindex]) {
            minindex = i;
        }
    }
    swap(candies[minindex], candies[maxindex]);
    for (int i = 0; i < n; i++) {
        cout << candies[i] << " ";
    }
    cout << "\n";
}
