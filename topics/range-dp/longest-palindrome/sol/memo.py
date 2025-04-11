#!/usr/bin/env python3

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)


def longest_palindromic_subsequence(word):
    n = len(word)

    memo = {(i, i): 1 for i in range(n)}

    def dp(i, j):
        try:
            return memo[(i, j)]
        except:
            if i > j:
                return 0
            if word[i] == word[j]:
                res = dp(i + 1, j - 1) + 2
                memo[(i, j)] = res
                return res
            else:
                res = max(dp(i + 1, j), dp(i, j - 1))
                memo[(i, j)] = res
                return res

    return dp(0, n - 1)


word = input().strip()
print(longest_palindromic_subsequence(word))
