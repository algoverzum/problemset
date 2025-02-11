#include <iostream>
#include <vector>
using namespace std;

int count_lower(vector<int> &nums, int barrier) {

    int count = 0;
    for (int num : nums) {
        if (num < barrier) {
            count++;
        }
    }

    return count;
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
