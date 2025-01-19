#!/usr/bin/env python3
# @check-accepted: *

n, m = map(int, input().split())
database = input().split()
queries = input().split()
result = []
for query in queries:
    if query in database:
        result.append(database.index(query) + 1)
    else:
        result.append(-1)
print(*result)
