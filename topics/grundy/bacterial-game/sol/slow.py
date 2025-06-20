#!/usr/bin/env python3


def solve_bacterial_game(grid, R, C):
    DIRS = {"H": [(0, -1), (0, 1)], "V": [(-1, 0), (1, 0)]}  # nyugat, kelet  # észak, dél

    def in_bounds(r, c):
        return 0 <= r < R and 0 <= c < C

    def spread(r, c, typ, board):
        visited = set()
        stack = [(r, c)]
        while stack:
            r0, c0 = stack.pop()
            for dr, dc in DIRS[typ]:
                nr, nc = r0 + dr, c0 + dc
                if in_bounds(nr, nc):
                    if board[nr][nc] == "#":
                        return None
                    if board[nr][nc] == "." and (nr, nc) not in visited:
                        board[nr][nc] = typ
                        visited.add((nr, nc))
                        stack.append((nr, nc))
        return board

    def serialize(board):
        return tuple(tuple(row) for row in board)

    memo = {}

    def dfs(state, turn):
        key = (state, turn)
        if key in memo:
            return memo[key]

        board = [list(row) for row in state]
        has_move = False

        for r in range(R):
            for c in range(C):
                if board[r][c] != ".":
                    continue

                for typ in ["H", "V"]:
                    new_board = [row[:] for row in board]
                    new_board[r][c] = typ
                    result = spread(r, c, typ, new_board)

                    if result is None:
                        continue

                    has_move = True
                    next_state = serialize(result)
                    if not dfs(next_state, 1 - turn):
                        memo[key] = True
                        return True

        memo[key] = False if has_move else False
        return memo[key]

    start_state = serialize(grid)
    return "Becca" if dfs(start_state, 0) else "Terry"


R, C = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]
print(solve_bacterial_game(grid, R, C))
