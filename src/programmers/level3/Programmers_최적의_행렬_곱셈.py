def solution(ms):

    # 행렬 내의 숫자 순서대로 d에 담는다
    d = [ms[0][0]] + [m[1] for m in ms]

    # M[i][j]는 (i - 1) 원소부터 j원소까지의 최소비용을 의미
    length = len(d)
    M = [[0] * length for _ in range(length)]

    # diag, i, j의 관계는 그림을 참조
    for diag in range(1, length):
        for i in range(1, length - diag):
            j = i + diag

            # i, j 사이의 k값을 순회하며 M[i][j]가 최소가 되게하는 k지점을 찾는다 (k 원소 왼쪽과 k원소 오른쪽을 곱셈함)
            M[i][j] = float("inf")
            for k in range(i, j):
                # 마지막에 붙은 건 M[i][k]와 M[k + 1][j]를 이어붙이는 비용이라고 보자
                M[i][j] = min(M[i][j], M[i][k] + M[k + 1][j] + d[i - 1] * d[k] * d[j])

    # 1 - 1 원소부터 length - 1 원소까지, 즉 첫 원소에서 마지막 원소까지 갈때의 비용
    return M[1][length - 1]

param1 = [[5,3],[3,10],[10,6]]

print(solution(param1)) # 270