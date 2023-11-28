# 주어진 모든 문제를 풀 수 있는 알고력과 코딩력을 얻는 최단시간
# 알고력, 코딩력 늘리기 위해 1의 시간 필요
# alp cop, 각각 알고력 코딩력
# problems 문제정보 담은 2차원배열 (100개 이하)
# [필요 알고력, 팔요 코딩력, 보상 알고력, 보상 코딩력, 소요시간]
import sys
import collections


def solution(alp, cop, problems):
    ALP_REQ, COP_REQ, ALP_RWD, COP_RWD, COST = range(5)

    my_solved = [False] * len(problems)
    my_unsolved_num = len(problems)

    global answer
    answer = float("inf")
    P_RANGE = range(len(problems))

    q = collections.deque()
    q.append([alp, cop, 0, my_solved, my_unsolved_num])
    while q:
        curr_alp, curr_cop, t, solved, unsolved_num = q.popleft()

        if t > answer:
            continue

        if unsolved_num == 0:
            answer = min(answer, t)
            continue

        solved_p = [[i, p] for i, p in enumerate(problems) if solved[i]]
        unsolved_p = [[i, p] for i, p in enumerate(problems) if not solved[i]]

        # 안 푼 문제 중 바로 풀 수 있는 문제면 풀어버림
        # 바로 못 푸는 건 알고력 코딩력 늘려서 시도
        for i, p in unsolved_p:
            next_solved = solved[:]
            next_solved[i] = True
            extra_alp = max(0, p[ALP_REQ] - curr_alp)
            extra_cop = max(0, p[COP_REQ] - curr_cop)
            q.append(
                [curr_alp + extra_alp, curr_cop + extra_cop, t + extra_alp + extra_cop, next_solved, unsolved_num - 1])

        # 푼 문제들 다시 한 번 더 풀어봄
        for i, p in solved_p:
            q.append([curr_alp + p[ALP_RWD], curr_cop + p[COP_RWD], t + p[COST], solved[:], unsolved_num])

    return answer


param11, param12, param13 = 10, 10, [[10,15,2,1,2],[20,20,3,3,4]]
param21, param22, param23 = 0,0,[[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]

print(solution(param11, param12, param13)) # 15
print(solution(param21, param22, param23)) # 13