#include <iostream>
#include <vector>
using namespace std;

int count_lower(vector<int> &nums, int barrier) {

    // Write your code here

    return 0;
}

// Do not change anything below!!!
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    int count;
    count = count_lower(nums, k);
    cout << count << "\n";
}
