#!/usr/bin/env python3
# @check-accepted: examples small all


def longest_common_substring(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    max_len = 0
    end_index_s1 = 0

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_index_s1 = i

    return s1[end_index_s1 - max_len : end_index_s1]


word1 = input()
word2 = input()
print(len(longest_common_substring(word1, word2)))
