#include <iostream>
#include <vector>
using namespace std;

int first_even(vector<int> &nums) {

    // Write your code here
}

// Do not change anything below!!!
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
