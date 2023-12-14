# 신청한 순서대로 방을 배정
# 요청한 방에 먼저 배정. 없다면 더 번호가 큰 방 중 제일 번호가 작은 방

import bisect, math


def solution(k, room_number):
    answer = []
    TOTAL_EXP = int(math.log10(k)) if k % 10 == 0 else int(math.log10(k)) + 1
    SIZE_EXP = TOTAL_EXP // 2
    PAGE_EXP = TOTAL_EXP - SIZE_EXP
    PAGE_NUM = 10 ** PAGE_EXP
    SIZE = 10 ** SIZE_EXP

    # PAGE_NUM = 10
    # SIZE = 1

    rooms = [[i + 1 for i in range(j * SIZE, (j + 1) * SIZE)] for j in range(PAGE_NUM)]
    # print(rooms)

    for num in room_number:
        page_idx = num // SIZE if num % SIZE != 0 else num // SIZE - 1
        while not rooms[page_idx] or (idx:= bisect.bisect_left(rooms[page_idx], num)) == len(rooms[page_idx]):
            page_idx += 1
        page = rooms[page_idx]
        answer.append(page[idx])
        page.pop(idx)
        # print(num, page_idx, idx, page)


    return answer


print(solution(10,	[1,3,4,1,3,1]))
# param2 = [1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1,1,3,4,1,3,1]
# param2 = list([50] * 101)
# print(solution(len(param2) + 100, param2))