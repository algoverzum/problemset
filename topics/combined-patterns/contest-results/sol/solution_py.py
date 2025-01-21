#!/usr/bin/env python3
# @check-accepted: *

n, q = map(int, input().split())
result = input().split()
queries = input().split()
for query in queries:
    if query in result:
        print(result.index(query) + 1, end=" ")
    else:
        print(-1, end=" ")
