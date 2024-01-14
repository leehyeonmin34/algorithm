# 싱글(x1), 더블(x2), 트리플(x3), 불(50)
# 정확히 0점으로 만드는 사람이 win
# 같은 라운드에 0점을 만들면 "싱글" 혹은 "불"을 더 많이 던진 사람이 승. 
# 그것마저 같다면 선공이 승.
# 목표점수 target 인자. 
# 최선의 [다트 수, 싱글 수 + 불 수]  
def solution(target):

    DART, STAR = range(2)
    dp = [[100000, 0] for _ in range(target + 1)]
    dp[0] = [0,0]

    # 충분히 큰 숫자에선 60으로 처리하는
    count = (target - 1000) // 60
    target -= count * 60
    # while target > 1000:
    #     target -= 60
    #     count += 1

    def update(curr, hit, star):
        next = curr + hit
        if next <= target:
            if dp[next][DART] > dp[curr][DART] + 1 or dp[next][DART] == dp[curr][DART] + 1 and dp[next][STAR] < dp[curr][STAR] + star:
                dp[next] =[dp[curr][DART] + 1, dp[curr][STAR] + star]

    for i in range(0, target + 1):
        for j in range(1, 21):
            update(i, j * 1, 1)
            update(i, j * 2, 0)
            update(i, j * 3, 0)

        update(i, 50, 1)

    dp[target][DART] += count
    return dp[target]


print(solution(21)) # [1,0]
print(solution(58)) # [2,2]