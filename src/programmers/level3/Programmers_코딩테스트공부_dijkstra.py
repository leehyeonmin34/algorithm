# 주어진 모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단시간
# 알고력, 코딩력 늘리기 위해 1의 시간 필요
# alp cop, 각각 알고력 코딩력
# problems 문제정보 담은 2차원배열 (100개 이하)
# [필요 알고력, 팔요 코딩력, 보상 알고력, 보상 코딩력, 소요시간]
# 주어진 모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단시간
# 알고력, 코딩력 늘리기 위해 1의 시간 필요
# alp cop, 각각 알고력 코딩력
# problems 문제정보 담은 2차원배열 (100개 이하)
# [필요 알고력, 팔요 코딩력, 보상 알고력, 보상 코딩력, 소요시간]
# 주어진 모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단시간
# 알고력, 코딩력 늘리기 위해 1의 시간 필요
# alp cop, 각각 알고력 코딩력
# problems 문제정보 담은 2차원배열 (100개 이하)
# [필요 알고력, 팔요 코딩력, 보상 알고력, 보상 코딩력, 소요시간]
import sys
import collections

import heapq

def solution(alp, cop, problems):
    max_alp, max_cop = max(x[0] for x in problems), max(x[1] for x in problems)

    problems += [[0, 0, 1, 0, 1], [0, 0, 0, 1, 1]]

    table = [[int(1e9) for _ in range(151)] for _ in range(151)]
    table[alp][cop] = 0

    h = [(0, alp, cop)]
    while h:
        # cost 제일 적은 거 추출
        curr_cost, curr_alp, curr_cop = heapq.heappop(h)

        # 최고 문제 풀수 있으면 끝
        if curr_alp >= max_alp and curr_cop >= max_cop:
            return curr_cost

        # 이미 해당 지점(curr_alp, curr_cop)을 다른 최단경로가 방문했다면 무시
        if table[curr_alp][curr_cop] < curr_cost:
            continue

        # 다음으로 풀 문제가 table의 값인 최소 cost를 갱신할 수 있다면 힙에 넣기
        # 풀 문제가 없다면 코딩력, 알고력을 공부할게 될 것임 (problems에 추가해놓았으니)
        for r_alp, r_cop, a_alp, a_cop, n_cost in problems:
            n_alp, n_cop = min(150, curr_alp + a_alp), min(150, curr_cop + a_cop)
            if curr_alp >= r_alp and curr_cop >= r_cop and curr_cost + n_cost < table[n_alp][n_cop]:
                table[n_alp][n_cop] = curr_cost + n_cost
                heapq.heappush(h, (curr_cost + n_cost, n_alp, n_cop))




param11, param12, param13 = 10, 10, [[10,15,2,1,2],[20,20,3,3,4]]
param21, param22, param23 = 0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

print(solution(param11, param12, param13)) # 15
print(solution(param21, param22, param23)) # 13
