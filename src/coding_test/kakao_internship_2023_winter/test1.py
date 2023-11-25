
# 주고받은 수 다르면, 준 횟수 큰 사람 <- 적은 사람
# 주고받은 수가 같다면, 선물지수 큰 사람 <- 낮은 사람
# 선물지수는 내가 준 선물 수 - 내가 받은 선물 수
# 선물을 가장 많이 받을 친구가 받을 선물 수
#gifts의 'a b'에서 a -> b

from collections import defaultdict

from itertools import combinations


def solution(friends, gifts):
    present_degree = defaultdict(int)
    present_num = defaultdict()
    present_to_get = defaultdict(int)

    for friend in friends:
        present_num[friend] = defaultdict(int)

    for gift in gifts:
        giver, reciever = gift.split(" ")
        present_num[giver][reciever] += 1
        present_degree[giver] += 1
        present_degree[reciever] -= 1

    for a, b in combinations(friends, 2):
        a_num = present_num[a][b]
        b_num = present_num[b][a]

        if a_num > b_num:
            present_to_get[a] += 1
        elif a_num < b_num:
            present_to_get[b] += 1
        else:
            if present_degree[a] > present_degree[b]:
                present_to_get[a] += 1
            elif present_degree[a] < present_degree[b]:
                present_to_get[b] += 1

    answer_list = [present_to_get[key] for key in present_to_get.keys()]
    if not answer_list:
        return 0
    else:
        return max(answer_list)


param1_1 = ["muzi", "ryan", "frodo", "neo"]
param1_2 = ["muzi frodo", "muzi forodo", "ryan muzi","ryan muzi","ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

param2_1 = ["a", "b", "c"]
param2_2 = ["a b", "b a", "a c", "a c", "c a", "c a"]

# print(solution(param1_1, param1_2)) # 2
print(solution(param2_1, param2_2)) # 0