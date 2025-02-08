// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

vector<int> odd_numbers(vector<int> &nums) {
    vector<int> odds;
    for (auto &num : nums) {
        if (num % 2 == 1) {
            odds.push_back(num);
        }
    }

    return odds;
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    vector<int> odds;
    odds = odd_numbers(nums);
    for (auto &odd : odds) {
        cout << odd << " ";
    }
    cout << "\n";
}
