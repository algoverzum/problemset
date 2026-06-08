#!/usr/bin/env pypy3

from sys import stdin

input = stdin.readline


class SegmentTree:
    def __init__(self, List):
        n = len(List)
        self.tree = [0 for i in range(2 * n)]

        for i in range(n):
            self.tree[i + n] = List[i]

        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def add(self, pos):
        n = len(self.tree) // 2

        i = pos + n
        self.tree[i] += 1

        j = i
        while j > 1:
            self.tree[j >> 1] = self.tree[j] + self.tree[j ^ 1]
            j >>= 1

    def sumInRange(self, left, right):
        n = len(self.tree) // 2
        result = 0
        left += n
        right += n

        while left < right:
            if left & 1:
                result += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                result += self.tree[right]

            left >>= 1
            right >>= 1

        return result


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    res = 0
    segmentTree = SegmentTree([0] * (10**6 + 1))
    for a in A:
        segmentTree.add(a)
        res += segmentTree.sumInRange(a + 1, 10**6 + 1)
    print(res)


for _ in range(int(input())):
    solve()
