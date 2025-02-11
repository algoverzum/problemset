#!/usr/bin/env python3.12
# @check-accepted: *
def find_par(par, r):
    if par[r] == r:
        return r
    else:
        par[r] = find_par(par, par[r])
        return par[r]


n = int(input())
in_degree = [0] * 26
out_degree = [0] * 26
par = list(range(26))
for _ in range(n):
    word = input().strip()
    u = ord(word[0]) - ord("a")
    v = ord(word[-1]) - ord("a")
    in_degree[v] += 1
    out_degree[u] += 1
    u_par = find_par(par, u)
    v_par = find_par(par, v)
    if u_par != v_par:
        par[u_par] = v_par

unique_parents = set(find_par(par, i) for i in range(26) if in_degree[i] > 0 or out_degree[i] > 0)
single = len(unique_parents) == 1
pos1, mns1, other = 0, 0, 0
if single:
    for i in range(26):
        diff = in_degree[i] - out_degree[i]
        if diff == 1:
            pos1 += 1
        elif diff == -1:
            mns1 += 1
        elif diff != 0:
            other += 1

if single and other == 0 and ((pos1 == 0 and mns1 == 0) or (pos1 == 1 and mns1 == 1)):
    print("YES")
else:
    print("NO")
