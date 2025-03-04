// @check-accepted: *
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int binary_search(const string &word, const vector<string> &list)
{
    int l = 0;
    int r = int(list.size()) - 1;
    while (l <= r)
    {
        int mid = l + (r - l) / 2;
        if (list[mid] == word)
        {
            return mid;
        }
        else if (list[mid] < word)
        {
            l = mid + 1;
        }
        else
        {
            r = mid - 1;
        }
    }
    return -1;
}

int main()
{
    int n;
    cin >> n;

    vector<string> english_words(n);
    vector<string> alien_words(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> english_words[i] >> alien_words[i];
    }

    int m;
    cin >> m;
    vector<string> message(m);
    for (int i = 0; i < m; ++i)
    {
        cin >> message[i];
    }

    for (const string &word : message)
    {
        int idx = binary_search(word, english_words);
        cout << alien_words[idx] << "\n";
    }

    return 0;
}