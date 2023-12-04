# 정확도 테스트
# 테스트 1 〉	통과 (0.21ms, 10.4MB)
# 테스트 2 〉	통과 (0.92ms, 10.4MB)
# 테스트 3 〉	통과 (0.21ms, 10.4MB)
# 테스트 4 〉	통과 (0.37ms, 10.5MB)
# 테스트 5 〉	통과 (0.21ms, 10.5MB)
# 테스트 6 〉	통과 (0.21ms, 10.5MB)
# 테스트 7 〉	통과 (0.21ms, 10.4MB)
# 테스트 8 〉	통과 (0.21ms, 10.3MB)
# 테스트 9 〉	통과 (0.10ms, 10.5MB)
# 테스트 10 〉	통과 (0.03ms, 10.5MB)

# 효율성  테스트
# 테스트 1 〉	통과 (114.78ms, 10.7MB)
# 테스트 2 〉	통과 (110.47ms, 10.7MB)
# 테스트 3 〉	통과 (112.55ms, 10.7MB)
# 테스트 4 〉	통과 (115.92ms, 10.7MB)
# 테스트 5 〉	통과 (124.00ms, 10.8MB)
# 테스트 6 〉	통과 (112.67ms, 10.8MB)
# 테스트 7 〉	통과 (110.01ms, 10.7MB)
# 테스트 8 〉	통과 (124.12ms, 10.7MB)


def solution(arr):

    # 숫자와 연산자를 분리
    d = [int(item) for item in arr if item.isdigit()]
    op = [item for item in arr if not item.isdigit()]

    lend = len(d)

    # 최댓값과 최솟값을 담은 dp를 활용
    # dp[i][j]는 d의 i원소부터 j원소까지의 연산의 최댓값/최솟값을 적을 것임
    max_dp = [[-10 ** 9] * len(d) for _ in range(lend)]
    min_dp = [[10 ** 9] * len(d) for _ in range(lend)]

    # dp[i][i]는 연산 없이 i원소 자신
    for i in range(lend):
        max_dp[i][i] = d[i]
        min_dp[i][i] = d[i]


    for diag in range(1, lend):
        for i in range(0, lend - diag):
            j = i + diag

            for k in range(i, j):
                M = 0
                m = 0
                if op[k] == "+": # 더하기일때 최댓값과 최솟값!
                    M = max_dp[i][k] + max_dp[k + 1][j]
                    m = min_dp[i][k] + min_dp[k + 1][j]
                else: # 빼기일때 최댓값과 최솟값!
                    M = max_dp[i][k] - min_dp[k + 1][j]
                    m = min_dp[i][k] - max_dp[k + 1][j]

                # 최대, 최소 갱신
                max_dp[i][j] = max(max_dp[i][j], M)
                min_dp[i][j] = min(min_dp[i][j], m)

    return max_dp[0][-1]


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[:7:1]) # [0, 1, 2, 3, 4, 5, 6]
print(a[:7:2]) # [0, 2, 4, 6]
print(a[:7:3]) # [0, 3, 6]
print(a[:7:4]) # [0, 4]

print(a[:9:1]) # [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(a[:9:2]) # [0, 2, 4, 6, 8]
print(a[:9:3]) # [0, 3, 6]
print(a[:9:4]) # [0, 4, 8]


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[2:7:1]) #[2, 3, 4, 5, 6]
print(a[2:7:2]) # [2, 4, 6]
print(a[2:7:3]) # [2, 5]
print(a[2:7:4]) # [2, 6]



a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a[:8:]) # [0, 1, 2, 3, 4, 5, 6, 7]
print(a[::3]) # [0, 3, 6, 9]
print(a[::]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[:0:-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1]
