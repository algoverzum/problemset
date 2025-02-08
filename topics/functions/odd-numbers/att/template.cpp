#include <iostream>
#include <vector>
using namespace std;

vector<int> odd_numbers(vector<int> &nums) {

    // Write your code here

    return vector<int>();
}

// Do not change anything below!!!
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
