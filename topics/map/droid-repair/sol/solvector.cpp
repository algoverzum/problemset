// @check-accepted: examples
// @check-time-limit-exceeded: all
#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> droids;

    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;

        for (int j = 0; j < droids.size(); ++j) {
            if (droids[j] == num) {
                std::cout << j << " " << i << std::endl;
                return 0;
            }
        }

        droids.push_back(num);
    }

    std::cout << -1 << std::endl;
    return 0;
}
