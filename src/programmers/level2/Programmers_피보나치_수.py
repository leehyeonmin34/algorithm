def solution(n):
    dp = [0, 1]

    if n < 2:
        return dp[n]

    i = 2
    while i <= n:
        dp = [dp[1], dp[0] + dp[1]]
        i += 1

    return dp[-1] % 1234567