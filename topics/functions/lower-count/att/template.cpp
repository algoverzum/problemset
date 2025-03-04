#include <iostream>
#include <vector>
using namespace std;

// Create a count_lower function here

// Do not change anything below!!!
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    cout << count_lower(nums, k) << "\n";
}
