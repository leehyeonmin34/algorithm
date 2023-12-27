# 신청한 순서대로 방을 배정
# 요청한 방에 먼저 배정. 없다면 더 번호가 큰 방 중 제일 번호가 작은 방

import bisect, math


def solution(k, room_number):
    k = min(k, max(room_number) + len(room_number) + 10)

    answer = []
    TOTAL_EXP = int(math.log2(k)) + 1
    SIZE_EXP = TOTAL_EXP * 4 // 5
    PAGE_EXP = TOTAL_EXP - SIZE_EXP
    PAGE_NUM = 2 ** PAGE_EXP
    SIZE = 2 ** SIZE_EXP

    # PAGE_NUM = 10
    # SIZE = 1

    rooms = [[i + 1 for i in range(j * SIZE, (j + 1) * SIZE)] for j in range(PAGE_NUM)]

    for num in room_number:
        page_idx = num // SIZE if num % SIZE != 0 else num // SIZE - 1
        while not rooms[page_idx] or rooms[page_idx][-1] < num:
            page_idx += 1
        idx = bisect.bisect_left(rooms[page_idx], num)
        page = rooms[page_idx]
        answer.append(page[idx])
        page.pop(idx)

    return answer


print(solution(10,	[1,3,4,1,3,1]))
# param2 = [1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1]
# param2 = list([50] * 101)
# print(solution(len(param2) + 100, param2))