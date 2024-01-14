# 회전판에 n개의 음식
# 1초씩 음식을 섭취하고 다음으로 넘어감
# 먹방 시작한지 k초 후에 방송중단, 네트워크 정상화 후 몇번 음식부터 섭취해야하는지 알고자 함
# 그러니까 k초에 먹어야할 음식을 알고싶음.
# 섭취할 음식 없다면 -1 리턴

import bisect
def solution(food_times, k):
    TIME, INDEX = 0, 1
    N = len(food_times)

    a = sorted([[t, i] for (i, t) in enumerate(food_times)])

    h = 0
    for i, food in enumerate(a):
        h, prev_h = food[TIME], h
        line = N - i

        if h == prev_h:
            continue

        area_val = (h - prev_h) * line
        if k >= area_val:
            k -= area_val

        else:
            foods_left = [i for i, t in enumerate(food_times) if t > prev_h]
            return foods_left[k % len(foods_left)]  + 1

    return -1

p1, p2 = [3, 1, 2],	5, #1
p21, p22 = [1, 1, 4, 5, 6, 3], 14 #3
p31, p32 = [1, 1, 4, 5, 6, 3], 13 #6
p41, p42 = [1, 5, 5, 5, 5, 6, 7], 31 # 6

print(solution(p1,p2))
print(solution(p21,p22))
print(solution(p31,p32))
print(solution(p41,p42))