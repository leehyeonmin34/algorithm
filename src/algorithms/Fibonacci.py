# 반복
def solution(n):
    curr, prev, prev2 = 2, 1, 1
    for i in range(3, n + 1):
        curr, prev, prev2 = curr + prev, curr, prev
        print(curr, prev, prev2)
    return curr

# dp
# def solution(n):
#     dp = [0] * (n + 1)
#     dp[0], dp[1] = 1, 1
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#
#     print(dp)
#     return dp[n]

# 재귀
# def solution(n):
#
#     if n in [1,2]:
#         return 1
#
#     return solution(n - 1) + solution(n - 2)
#
# print(solution(10))

print(solution(10))