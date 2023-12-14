# 신청한 순서대로 방을 배정
# 요청한 방에 먼저 배정. 없다면 더 번호가 큰 방 중 제일 번호가 작은 방

import bisect

def solution(k, room_number):

    rooms = [i for i in range(1, k + 1)]

    answer = []
    for num in room_number:
        idx = bisect.bisect_left(rooms, num)
        answer.append(rooms[idx])
        rooms.pop(idx)

    return answer


print(solution(10,	[1,3,4,1,3,1]))