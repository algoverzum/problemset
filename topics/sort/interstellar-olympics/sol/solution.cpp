// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<std::tuple<int, int, int, int>> medals;

    for (int i = 0; i < n; ++i) {
        int gold, silver, bronze;
        std::cin >> gold >> silver >> bronze;

        medals.emplace_back(-gold, -silver, -bronze, i + 1);
    }

    std::sort(medals.begin(), medals.end());

    for (const auto &m : medals) {
        std::cout << std::get<3>(m) << " ";
    }

    std::cout << std::endl;

    return 0;
}
