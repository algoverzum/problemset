// @check-accepted: *
#include <iostream>
#include <vector>
using namespace std;

int first_even(vector<int> &nums) {
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] % 2 == 0) {
            return i + 1;
        }
    }
    return -1;
}
int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    int first = first_even(nums);

    cout << first << "\n";
}
