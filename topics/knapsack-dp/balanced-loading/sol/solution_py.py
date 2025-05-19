#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
weights = [0] + list(map(int, input().split()))
total_sum = sum(weights)

target = total_sum // 2
dp = [[False] * (target + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(target + 1):
        dp[i][j] = dp[i - 1][j] or (j >= weights[i] and dp[i - 1][j - weights[i]])

left = target
while not dp[n][left]:
    left -= 1

used = [False] * (n + 1)
j = left
for i in range(n, 0, -1):
    if j >= weights[i] and not dp[i - 1][j]:
        used[i] = True
        j -= weights[i]

left_cargo = [i for i in range(1, n + 1) if used[i]]
right_cargo = [i for i in range(1, n + 1) if not used[i]]

print(total_sum - 2 * left)
print(len(left_cargo), *left_cargo)
print(len(right_cargo), *right_cargo)
