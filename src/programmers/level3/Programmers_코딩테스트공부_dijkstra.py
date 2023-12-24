

# 정확성  테스트
# 테스트 1 〉	통과 (0.24ms, 10.3MB)
# 테스트 2 〉	통과 (0.22ms, 10.2MB)
# 테스트 3 〉	통과 (0.09ms, 10.4MB)
# 테스트 4 〉	통과 (0.06ms, 10.3MB)
# 테스트 5 〉	통과 (0.18ms, 10.4MB)
# 테스트 6 〉	통과 (0.23ms, 10.4MB)
# 테스트 7 〉	통과 (0.03ms, 10.2MB)
# 테스트 8 〉	통과 (0.03ms, 10.4MB)
# 테스트 9 〉	통과 (0.07ms, 10.3MB)
# 테스트 10 〉	통과 (0.04ms, 10.4MB)

# 효율성  테스트
# 테스트 1 〉	통과 (25.39ms, 10.6MB)
# 테스트 2 〉	통과 (77.07ms, 10.5MB)
# 테스트 3 〉	통과 (4.96ms, 10.3MB)
# 테스트 4 〉	통과 (17.78ms, 10.3MB)
# 테스트 5 〉	통과 (19.09ms, 10.5MB)
# 테스트 6 〉	통과 (6.33ms, 10.4MB)
# 테스트 7 〉	통과 (16.52ms, 10.7MB)
# 테스트 8 〉	통과 (19.41ms, 10.3MB)
# 테스트 9 〉	통과 (87.56ms, 11.2MB)
# 테스트 10 〉	통과 (7.45ms, 10.4MB)

# 주어진 모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단시간
# 알고력, 코딩력 늘리기 위해 1의 시간 필요
# alp cop, 각각 알고력 코딩력
# problems 문제정보 담은 2차원배열 (100개 이하)
# [필요 알고력, 팔요 코딩력, 보상 알고력, 보상 코딩력, 소요시간]

import heapq

def solution(alp: int, cop: int, problems: list):
    problems.append([0, 0, 1, 0, 1]) # 알고력 +1
    problems.append([0, 0, 0, 1, 1]) # 코딩력 +1

    ALP_REQ, COP_REQ, ALP_RWD, COP_RWD, COST = range(5)
    MAX_ALP = max(alp, max([p[ALP_REQ] for p in problems]))
    MAX_COP = max(cop, max([p[COP_REQ] for p in problems]))

    # costs[alp][cop] = (alp,cop)의 실력을 갖기 위한 최소 cost
    costs = [[float("inf")] * (MAX_COP + 1) for _ in range(MAX_ALP + 1)]
    costs[alp][cop] = 0
    q = [[0, alp, cop]]

    while q:
        curr_cost, curr_alp, curr_cop = heapq.heappop(q)

        # 최대 알고력, 코딩력에 도달했다면 그게 최솟값이므로 반환
        if curr_alp >= MAX_ALP and curr_cop >= MAX_COP:
            return curr_cost

        # 이미 방문한 지점이라면 중지
        if costs[curr_alp][curr_cop] < curr_cost:
            continue

        # [*중요*]
        # 이 지점에서 costs[curr_alp][curr_cop] = curr_cost로 지정하는 것보다,
        # 아래 heapq에 넣기 전에 지정하는 게 훨씬 더 빠름

        for p in problems:
            alp_req, cop_req, alp_rwd, cop_rwd, cost = p

            # 문제 p를 풀 수 있다면 풀어버린 경우를 q에 넣자
            if alp_req <= curr_alp and cop_req <= curr_cop:
                next_alp = min(MAX_ALP, curr_alp + alp_rwd)
                next_cop = min(MAX_COP, curr_cop + cop_rwd)
                next_cost = curr_cost + cost

                # [*중요*]
                # 여기서도 이미 방문한 지점이면 중지하는 if문을 넣으면 훨씬 빠르다.
                # 아무래도 힙에서 추출하려면 logN 시간이 필요하기 때문에, 힙에 뭔가를 최대한 안 넣게 되기 때문인 것 같다.
                # 여기서 costs값 갱신
                if costs[next_alp][next_cop] > next_cost:
                    costs[next_alp][next_cop] = next_cost
                    heapq.heappush(q, [next_cost, next_alp, next_cop])




param11, param12, param13 = 10, 10, [[10,15,2,1,2],[20,20,3,3,4]]
param21, param22, param23 = 0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

print(solution(param11, param12, param13)) # 15
print(solution(param21, param22, param23)) # 13

