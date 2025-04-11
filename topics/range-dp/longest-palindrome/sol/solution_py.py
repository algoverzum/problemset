#!/usr/bin/env python3
# @check-accepted: *


def longest_palindromic_subsequence(word):
    n = len(word)

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if word[i] == word[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


word = input()
print(longest_palindromic_subsequence(word))
