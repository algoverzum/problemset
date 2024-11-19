#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
    int T;
    std::cin >> T;
    while (T--) {
        int n;
        std::cin >> n;
        std::string s;
        std::cin >> s;
        std::vector<int> len;
        int l = 0;
        for (auto x : s) {
            if (x == '-' && l > 0) {
                len.push_back(l);
                l = 0;
            } else if (x == '.')
                ++l;
        }
        if (l > 0)
            len.push_back(l);
        int ans = 0;
        std::sort(len.rbegin(), len.rend());
        for (int i = 0; i < len.size(); ++i)
            ans = std::max(len[i] / 2 + i + 1, ans);
        std::cout << len.size() << ' ' << ans << std::endl;
    }
}
