#!/usr/bin/env python3

memo = {}


def avmoves(r, c, board):
    row = []
    col = []
    for rr in range(r):
        joe = True
        for cc in range(c):
            if board[rr * c + cc] == "#":
                joe = False
                break
        if joe:
            row.append(rr)
    for cc in range(c):
        joe = True
        for rr in range(r):
            if board[rr * c + cc] == "#":
                joe = False
                break
        if joe:
            col.append(cc)
    return row, col


def grundy(r, c, board):
    if r == 0 or c == 0:
        return 0
    elif (r, c, board) in memo:
        return memo[(r, c, board)]
    arow, acol = avmoves(r, c, board)
    if arow == [] and acol == []:
        memo[(r, c, board)] = 0
        return 0
    grval = []
    for rr in arow:
        newboard1 = ""
        newboard2 = ""
        for rrr in range(r):
            if rrr < rr:
                newboard1 += board[rrr * c : (rrr + 1) * c]
            elif rrr > rr:
                newboard2 += board[rrr * c : (rrr + 1) * c]
        grval.append(grundy(rr, c, newboard1) ^ grundy(r - rr - 1, c, newboard2))
    for cc in acol:
        newboard1 = ""
        newboard2 = ""
        for rrr in range(r):
            newboard1 += board[rrr * c : rrr * c + cc]
            newboard2 += board[rrr * c + cc + 1 : (rrr + 1) * c]
        grval.append(grundy(r, cc, newboard1) ^ grundy(r, c - cc - 1, newboard2))
    if 0 not in grval:
        memo[(r, c, board)] = 0
        return 0
    # mex
    for j in range(1, len(grval) + 1):
        if j not in grval:
            memo[(r, c, board)] = j
            return j


r, c = [int(s) for s in input().split()]
board = ""
for p in range(r):
    y = input().strip()
    board += y
if grundy(r, c, board) == 0:
    print("Terry")
else:
    print("Becca")
