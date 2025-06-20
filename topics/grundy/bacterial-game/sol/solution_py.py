#!/usr/bin/env python3
# @check-accepted: *


def solve_bacterial_game(grid, R, C):
    memo = {}

    def mex(s):
        m = 0
        while m in s:
            m += 1
        return m

    def is_row_empty(r, c1, c2):
        if c1 < c2:
            return all(grid[r][c] == "." for c in range(c1, c2))
        return False

    def is_col_empty(c, r1, r2):
        if r1 < r2:
            return all(grid[r][c] == "." for r in range(r1, r2))
        return False

    def grundy(r1, r2, c1, c2):
        key = (r1, r2, c1, c2)
        if key in memo:
            return memo[key]

        gset = set()

        # H-move
        for r in range(r1, r2):
            if is_row_empty(r, c1, c2):
                top = grundy(r1, r, c1, c2)
                bottom = grundy(r + 1, r2, c1, c2)
                gset.add(top ^ bottom)

        # V-move
        for c in range(c1, c2):
            if is_col_empty(c, r1, r2):
                left = grundy(r1, r2, c1, c)
                right = grundy(r1, r2, c + 1, c2)
                gset.add(left ^ right)

        result = mex(gset)
        memo[key] = result
        return result

    if grundy(0, R, 0, C) == 0:
        return "Terry"
    return "Becca"


R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]
print(solve_bacterial_game(grid, R, C))
