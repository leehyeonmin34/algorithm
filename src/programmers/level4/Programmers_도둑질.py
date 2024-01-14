def solution(money):
    LEN = len(money)

    def get_benefit(mon):
        dp = [0] * LEN
        dp[0] = mon[0]
        dp[1] = max(mon[0], mon[1])

        for i in range(2, LEN):
            dp[i] = max(dp[i - 1], dp[i - 2] + mon[i])
        return dp

    dp1 = get_benefit(money)
    dp2 = get_benefit(money[1:] + [money[0]])

    return max(dp1[-2], dp2[-4] + money[-1])

print(solution([1, 2, 3, 1])) #4