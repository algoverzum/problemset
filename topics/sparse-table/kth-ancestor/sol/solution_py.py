def kthancestor(v, x, k):
    for i in range(19):
        if x == -1:
            break
        if k & (1 << i):
            x = v[x][i]
    return x


n = int(input())
v = [[-1] * 19 for i in range(n + 1)]
q = int(input())

for i in range(q):
    query = list(map(int, input().split()))
    type = query[0]

    if type == 0:
        y, x = query[1], query[2]
        v[x][0] = y
        for j in range(1, 19):
            if v[x][j - 1] != -1:
                v[x][j] = v[v[x][j - 1]][j - 1]
            else:
                break
    elif type == 1:
        x = query[1]
        v[x][0] = -1
        for j in range(1, 19):
            v[x][j] = -1
    elif type == 2:
        x, k = query[1], query[2]
        ancestor = kthancestor(v, x, k)
        if ancestor == -1:
            ancestor = 0
        print(ancestor)
