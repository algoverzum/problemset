// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> nums(N);
    for (int i = 0; i < N; i++) {
        cin >> nums[i];
    }

    sort(nums.begin(), nums.end());

    for (int num : nums) {
        cout << num << "\n";
    }

    return 0;
}
