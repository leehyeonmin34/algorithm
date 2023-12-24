def solution(beginning, target):
    m = len(beginning)
    n = len(beginning[0])

    diff = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            diff[i][j] = beginning[i][j] ^ target[i][j]

    top = diff[0]
    reversed_top = [n ^ 1 for n in top]

    r = 0

    for i in range(1, m):
        if diff[i] == reversed_top:
            r += 1
        elif diff[i] != top:
            return -1

    c = sum(top)

    return min(r + c, m - r + n - c)

print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]],	[[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]])) #5
# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]],	[[1, 0, 1], [0, 0, 0], [0, 0, 0]])) # -1