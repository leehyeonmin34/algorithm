import collections

def solution(m, n, puddles):
    global result
    result = 0

    path = collections.defaultdict(int)
    path[(m, n)] = 1

    for i in range(m, 0, -1):
        for j in range(n, 0, -1):
            if i == m and j == n:
                path[(i, j)] = 1
            elif [i, j] in puddles or i < 0 or j < 0:
                path[(i, j)] = 0
            else:
                path[(i, j)] = path[(i + 1, j)] + path[(i, j + 1)]

    return path[1, 1] % 1000000007