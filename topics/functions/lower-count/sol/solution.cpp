#include <iostream>
#include <vector>
using namespace std;

int count_lower(vector<int> numbers, int limit) {
    int count = 0;
    for (int num : numbers) {
        if (num < limit) {
            count++;
        }
    }
    return count;
}

// Do not change anything below.
int main() {
    int n, k;
    cin >> n >> k;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    cout << count_lower(nums, k) << "\n";
}
