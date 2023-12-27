def solution(alp, cop, problems):

    inf = 10 ** 6
    problems.append([0,0,0,1,1])
    problems.append([0,0,1,0,1])
    max_alp, max_cop = max([i[0] for i in problems]), max([i[1] for i in problems])
    dp = [[inf for _ in range(max_alp + 1)] for _ in range(max_cop + 1)]
    if max_alp <= alp:
        alp = max_alp
    if max_cop <= cop:
        cop = max_cop
    dp[cop][alp] = 0

    # dp[cop][alp]에서 cop, alp의 값이 낮은 것부터 위로 올라갈수록 dp에 담긴 cost값도 올라감
    # 지나는 경로의 지점들의 높낮이가 정해져있을 경우 이렇게 반복문으로 풀어도되는 듯
    for i in range(cop, max_cop + 1):
        for j in range(alp, max_alp + 1):
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= cop_req and j >= alp_req:
                    k = i + cop_rwd if i + cop_rwd < max_cop else max_cop
                    l = j + alp_rwd if j + alp_rwd < max_alp else max_alp
                    dp[k][l] = min([dp[k][l], dp[i][j] + cost])
    return dp[-1][-1]


param11, param12, param13 = 10, 10, [[10,15,2,1,2],[20,20,3,3,4]]
param21, param22, param23 = 0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

print(solution(param11, param12, param13)) # 15
print(solution(param21, param22, param23)) # 13
