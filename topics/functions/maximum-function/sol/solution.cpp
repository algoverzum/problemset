// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int maximum(vector<int> v) {
    int maxi = v[0];
    for (int x : v) {
        if (x > maxi)
            maxi = x;
    }
    return maxi;
}

int main() {
    cout << maximum({3, 1, 4, 5, 2}) << "\n";
    cout << maximum({6, 5, 4, 3, 2, 1}) << "\n";
    cout << maximum({-4, -3, -2, -1}) << "\n";
    cout << maximum({0}) << "\n";
    cout << maximum({42, 42, 42, 42, 42, 42, 42}) << "\n";
    cout << maximum({100, 101, 100, 101, 100, 101}) << "\n";
    cout << maximum({3456, 8989, 432, 982, 3497, 34, 5430, 2134, 1092, 9997})
         << "\n";
}
