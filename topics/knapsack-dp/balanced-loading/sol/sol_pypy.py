#!/usr/bin/env pypy3
# @check-accepted: *

n = int(input())
weights = list(map(int, input().split()))

total = sum(weights)
dp = [False] * (total // 2 + 1)
dp[0] = True
prev = [-1] * (total // 2 + 1)

for t in range(n):
    for i in range(total // 2, weights[t] - 1, -1):
        if dp[i - weights[t]] and not dp[i]:
            dp[i] = True
            prev[i] = t

for left in range(total // 2, -1, -1):
    if dp[left]:
        break

used = [False] * n
curr = left
while curr > 0:
    task = prev[curr]
    used[task] = True
    curr -= weights[task]

left_cargo = [i + 1 for i in range(n) if used[i]]
right_cargo = [i + 1 for i in range(n) if not used[i]]

print(abs(total - 2 * left))
print(len(left_cargo), *left_cargo)
print(len(right_cargo), *right_cargo)
